import matplotlib.pyplot as plt
import numpy as np

import extras.functions as functions
import extras.parser as parser
import extras.utils as utils
from TP5.extras import plot_utils
from TP5.extras.config import Config
from TP5.perceptron.autoencoder import AutoEncoder


def create_ae(config: Config):
    full_dataset, _ = parser.parse_file(config.input, config.system_threshold)
    if config.normalize:
        full_dataset = utils.normalize(full_dataset)

    activation = functions.get_activation_functions(config.system, config.beta)
    dataset, subset = utils.extract_subset(full_dataset, config.training_ratio)

    ae = AutoEncoder(
        *activation,
        config.mid_layout,
        len(dataset[0]),
        config.latent_dim,
        config.momentum,
        config.alpha
    )
    if config.randomize_w:
        ae.randomize_weights(config.randomize_w_ref, config.randomize_w_by_len)
    return ae, full_dataset, dataset


def initialize_plot():
    plot_utils.init_plotter()
    plt.ion()
    plt.show()


def train_with_optimizer(config: Config, ae, dataset):
    dataset = utils.randomize(dataset, config.data_random_seed)
    ae.train_optimizer(
        dataset,
        dataset,
        config.trust,
        config.use_trust,
        config.optimizer,
        config.iter,
        config.fev
    )

    if config.plot:
        plot_utils.plot_values(range(len(ae.opt_err)), 'opt step', ae.opt_err, 'error', sci_y=False)


def train_normal(config: Config, ae, dataset):
    eps = []
    errors = []

    for epoch in range(config.epochs):
        dataset = utils.randomize(dataset, config.data_random_seed)

        for data in dataset:
            ae.train(data, data, config.eta)

        ae.update_weights()
        error = ae.error(dataset, dataset, config.trust, config.use_trust)

        if error < config.error_threshold:
            break

        if epoch % 50 == 0:
            print(f'epochs: {epoch}. Error: {error}')

        eps.append(epoch)
        errors.append(error)

    if config.plot:
        plot_utils.plot_values(eps, 'epoch', errors, 'error', sci_y=False)


def create_latent_space(config: Config, ae, dataset):
    data_labels = [
        '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
        'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_'
    ]

    le = np.array([ae.activation_to_latent_space(data) for data in dataset])
    plot_utils.plot_latent_space(le, data_labels, -1, 1)

    if config.plot:
        plt.pause(0.001)

    return data_labels


def ask_and_create_new_letter(ae, dataset, le, data_labels):
    print('################################')
    print('\nPara crear una nueva letra entre dos introduzca sus indices:')
    for i, l in enumerate(data_labels):
        print(str(i) + ': ' + str(l), end='\t')
        if i % 10 == 9:
            print('')

    i = int(input("\nPrimer indice: "))
    j = int(input("\nSegundo indice: "))

    new_le = np.sum([le[i], le[j]], axis=0) / 2
    new_letter = ae.activation_from_latent_space(new_le)

    plot_utils.print_pattern(dataset[i, 1:], 5)
    print('\n################################')
    plot_utils.print_pattern(dataset[j, 1:], 5)
    print('\n################################')
    print(new_letter)
    print('\n################################')
    plot_utils.print_pattern(np.around(new_letter[1:]), 5)


def main():
    config = parser.parse_config('config.json')

    ae, full_dataset, dataset = create_ae(config)

    if config.plot:
        initialize_plot()

    if config.optimizer is not None and config.optimizer != '':
        train_with_optimizer(config, ae, dataset)
    else:
        train_normal(config, ae, dataset)

    le, data_labels = create_latent_space(config, ae, full_dataset)

    while True:
        ask_and_create_new_letter(ae, full_dataset, le, data_labels)


if __name__ == '__main__':
    main()
