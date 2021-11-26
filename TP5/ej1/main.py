import json
import sys

import PIL.Image as Image
import matplotlib.pyplot as plt

from autoencoder import Autoencoder
from utils.config import Config
from utils.function import Function
from utils.methods import *


def create_image(X, name):
    S = X * 255
    array = np.array(S, dtype=np.uint8)
    img = Image.fromarray(array, mode="L").resize((X.shape[1] * 10, X.shape[0] * 10), Image.NEAREST)
    img.save(f"./results/{name}")


def print_symbol(X):
    config = Config()
    out_str = ""
    for i, s in enumerate(X):
        if i % config.width == 0 and i != 0:
            out_str += "\n"
        out_str += "*" if s >= 0.5 else " "
    print(out_str)


def main():
    config_file = "./configs/config.json"
    if len(sys.argv) >= 2:
        config_file = sys.argv[1]
    else:
        print(f"Using default config file {config_file}")

    file = open(config_file)
    config_dict = json.load(file)
    file.close()

    config = Config()
    config.setup_config(config_dict)

    # Load Dataset
    f = open(config.training_dataset)
    Y = np.empty((config.width * config.height, 0))

    line = f.readline()
    while line:
        image = []
        if line == "\n":
            line = f.readline()
            continue
        for i in range(config.height):
            line = line.replace("\n", "")
            line = [1 if char == "1" else 0 for char in line]
            image += line
            line = f.readline()
        image = np.array(image).reshape(-1, 1)
        Y = np.append(Y, image, 1)

    subset = (0, 31)
    Y = Y[:, subset[0]:subset[1]]

    X_train = np.copy(Y)
    Y_train = np.copy(Y)

    ae = Autoencoder(config.layers, config.latent_layer, Function(sigmoid, d_sigmoid), Function(error, d_error))
    ae.train(X_train, Y_train, epochs=config.epochs, batch_size=config.batch_size)

    X_test = np.copy(Y)
    if config.noise > 0:
        X_test = np.vectorize(
            lambda v: 1 - v if np.random.choice(a=[False, True], p=[1 - config.noise, config.noise]) else v)(Y)

    # Mappeo del cjto de entrenamiento al espacio latente
    latent_space = ae.encode(X_train)

    # Grafico de espacio latente
    plt.scatter(latent_space[0], latent_space[1])
    for i, label in enumerate(config.labels[subset[0]:subset[1]]):
        plt.annotate(label, (latent_space[0][i], latent_space[1][i]))
    plt.show(block=False)
    plt.figure()

    # Decodificacion del conjunto de prueba
    prediction = ae.feedforward(X_test)

    # Imagenes de letras (input y output)
    letters_per_row = 5
    letter_width = config.width
    letter_height = config.height
    image = np.ones((
        int(np.ceil(Y.shape[1] / letters_per_row)) * (letter_height + 1),
        letters_per_row * (letter_width + 1)))
    for i, p in enumerate(prediction.T):
        pp = p.reshape(letter_height, letter_width) < 0.5
        pp = pp.astype(int)
        ix = (i % letters_per_row) * (letter_width + 1)
        jy = (i // letters_per_row) * (letter_height + 1)
        image[jy:jy + letter_height, ix:ix + letter_width] = pp

    create_image(image, "output.png")

    image = np.ones((
        int(np.ceil(Y.shape[1] / letters_per_row)) * (letter_height + 1),
        letters_per_row * (letter_width + 1)))
    for i, p in enumerate(X_test.T):
        pp = p.reshape(letter_height, letter_width) < 0.5
        pp = pp.astype(int)
        ix = (i % letters_per_row) * (letter_width + 1)
        jy = (i // letters_per_row) * (letter_height + 1)
        image[jy:jy + letter_height, ix:ix + letter_width] = pp

    create_image(image, "input.png")

    while True:
        ask_and_create_new_letter(ae, Y, config.labels[subset[0]:subset[1]])

    # latent_code = ae.encode(X_train[:, 2][np.newaxis].T)
    # new_result = ae.decode(np.array([[x], [y]])).reshape((7, 5)) > 0.5

def ask_and_create_new_letter(ae: Autoencoder, dataset, data_labels):
    print('################################')
    print('\nPara crear una nueva letra entre dos introduzca sus indices:')
    for i, l in enumerate(data_labels):
        print(str(i) + ': ' + str(l), end='\t')
        if i % 10 == 9:
            print('')

    i = int(input("\nPrimer indice: "))
    j = int(input("\nSegundo indice: "))

    config = Config()
    dataset = dataset.T
    first_letter = ae.feedforward(dataset[i].reshape(config.height * config.width, 1), 0, config.latent_layer)
    second_letter = ae.feedforward(dataset[j].reshape(config.height * config.width, 1), 0, config.latent_layer)
    new_le = np.sum([first_letter, second_letter], axis=0) / 2

    new_letter = ae.feedforward(new_le, config.latent_layer)
    new_letter = new_letter.T[0] > 0.5
    new_letter = new_letter.astype(int)

    print('\n################################')
    print_symbol(dataset[i])
    print('\n################################')
    print_symbol(dataset[j])
    print('\n################################')
    print_symbol(new_letter)

if __name__ == "__main__":
    main()
