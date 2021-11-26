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

    Y_train = np.copy(Y)

    for noise in np.arange(0, 0.21, 0.1):
        ae = Autoencoder(config.layers, config.latent_layer, Function(sigmoid, d_sigmoid), Function(error, d_error))
        for i in range(20):
            print('iteration=', i, 'noise=', noise)
            X_noises = (np.vectorize(
                lambda v: 1 - v if np.random.choice(a=[False, True], p=[1 - noise, noise]) else v)(Y))
            ae.train(X_noises, Y_train, epochs=config.epochs, batch_size=config.batch_size)

        errors_x = []
        for i in range(20):
            X_noises = (np.vectorize(
                lambda v: 1 - v if np.random.choice(a=[False, True], p=[1 - noise, noise]) else v)(Y))
            X_predictions = ae.feedforward(X_noises)
            errors_x.append(np.sum(abs(X_predictions - Y_train), axis=0) / 35)
        plt.plot(np.mean(errors_x, axis=0), label=noise)

        X_noises = (np.vectorize(
            lambda v: 1 - v if np.random.choice(a=[False, True], p=[1 - noise, noise]) else v)(Y))
        X_predictions = ae.feedforward(X_noises)
        letters_per_row = 5
        letter_width = config.width
        letter_height = config.height
        image = np.ones((
            int(np.ceil(Y.shape[1] / letters_per_row)) * (letter_height + 1),
            letters_per_row * (letter_width + 1)))
        for i, p in enumerate(X_predictions.T):
            pp = p.reshape(letter_height, letter_width) < 0.5
            pp = pp.astype(int)
            ix = (i % letters_per_row) * (letter_width + 1)
            jy = (i // letters_per_row) * (letter_height + 1)
            image[jy:jy + letter_height, ix:ix + letter_width] = pp

        create_image(image, f"output_{noise}.png")

        image = np.ones((
            int(np.ceil(Y.shape[1] / letters_per_row)) * (letter_height + 1),
            letters_per_row * (letter_width + 1)))
        for i, p in enumerate(X_noises.T):
            pp = p.reshape(letter_height, letter_width) < 0.5
            pp = pp.astype(int)
            ix = (i % letters_per_row) * (letter_width + 1)
            jy = (i // letters_per_row) * (letter_height + 1)
            image[jy:jy + letter_height, ix:ix + letter_width] = pp

        create_image(image, f"input_{noise}.png")
    plt.xticks(range(len(config.labels)), config.labels)
    plt.legend(loc='upper right')
    plt.show()


if __name__ == "__main__":
    main()
