import matplotlib.pyplot as plt
import numpy as np
import sts as sts

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
        utils.generate_noise_dataset(dataset, config.den_pm),
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
            ae.train(utils.generate_noise(data, config.den_pm), data, config.eta)

        ae.update_weights()
        error = ae.error(utils.generate_noise_dataset(dataset, config.den_pm), dataset, config.trust, config.use_trust)

        if error < config.error_threshold:
            break

        if epoch % 50 == 0:
            print(f'epochs: {epoch}. Error: {error}')

        eps.append(epoch)
        errors.append(error)

    if config.plot:
        plot_utils.plot_values(eps, 'epoch', errors, 'error', sci_y=False)


def plot_results(config: Config, ae, dataset):
    data_labels = [
        '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
        'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_'
    ]

    pms = [config.den_pm / 4, config.den_pm, config.den_pm * 2.5]
    xs = []
    errors = []
    pms_labels = ['pm={:.04f}'.format(pm) for pm in pms]
    for pm_it in pms:
        emean = []
        for data in dataset:
            letter_emean_iter = []
            for i in range(50):
                noisy_activation = ae.activation(utils.generate_noise(data, pm_it))
                letter_emean_iter.append(np.sum(abs(np.around(noisy_activation[1:]) - data[1:])) / len(data[1:]))

            letter_emean = sts.mean(letter_emean_iter)
            emean.append(letter_emean)

        xs.append(range(len(dataset)))
        errors.append(emean)
        print(f'pm: {pm_it}, mean error: {sts.mean(emean)}')

    if config.plot:
        plot_utils.plot_multiple_values(
            xs,
            'Letter',
            errors,
            'Invalid bits',
            pms_labels,
            sci_y=False,
            xticks=data_labels,
            min_val_y=0,
            max_val_y=1
        )

        plot_utils.plot_stackbars(
            xs,
            'Letter',
            errors,
            'Invalid bits',
            pms_labels,
            sci_y=False,
            xticks=data_labels,
            min_val_y=0,
            max_val_y=1
        )


def main():
    config = parser.parse_config('config.json')

    ae, full_dataset, dataset = create_ae(config)

    if config.plot:
        initialize_plot()

    if config.optimizer is not None and config.optimizer != '':
        train_with_optimizer(config, ae, dataset)
    else:
        train_normal(config, ae, dataset)

    plot_results()


if __name__ == '__main__':
    main()
