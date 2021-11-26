import json
import sys

import matplotlib.pyplot as plt

from autoencoder import Autoencoder
from utils.config import Config
from utils.function import Function
from utils.methods import *


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

    ae1 = Autoencoder([35, 10, 2, 10, 35], 2, Function(sigmoid, d_sigmoid), Function(error, d_error))
    ae2 = Autoencoder([35, 20, 2, 20, 35], 2, Function(sigmoid, d_sigmoid), Function(error, d_error))
    ae3 = Autoencoder([35, 25, 15, 2, 15, 25, 35], 3, Function(sigmoid, d_sigmoid), Function(error, d_error))
    ae4 = Autoencoder([35, 25, 10, 5, 2, 5, 10, 25, 35], 4, Function(sigmoid, d_sigmoid), Function(error, d_error))
    aes = [ae1, ae2, ae3, ae4]
    errors = []
    for i, ae in enumerate(aes):
        errors.append([])
        for _ in range(1):
            errors[i].append(ae.train(X_train, Y_train, epochs=config.epochs, batch_size=config.batch_size))

    errors = np.mean(errors, axis=1)
    labels = ['35-10-2-10-35',
              '35-20-2-20-35',
              '35-25-15-2-15-25-35',
              '35-25-10-5-2-5-10-25-35'
              ]
    bar_positions = [i * 3 for i in range(len(labels))]
    plt.rcParams['font.size'] = '12'
    plt.figure(figsize=(10, 10))
    plt.bar(bar_positions, errors)
    plt.xticks(bar_positions, labels)
    plt.show()


if __name__ == "__main__":
    main()
