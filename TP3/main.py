import json
import random

import numpy as np

import data_parser
import utils
from TP3.perceptron import activation_functions
from TP3.perceptron.multilayer_perceptron import MultilayerPerceptron

config = {}


def parse_config():
    with open("config.json") as f:
        c = json.load(f)
    return c


def run():
    training_c = config['training']
    constants_c = config['constants']
    system_c = config['system']
    w_c = system_c['w']

    training, expected, n_type = data_parser.parse_files(training_c['input'], training_c['output'],
                                                         constants_c['system_threshold'])

    if system_c['function'] == "softmax":
        expected = utils.normalize_data(expected)
        fs = activation_functions.get_softmax_activation_function(constants_c['beta'])
    else:
        fs = activation_functions.get_step_activation_function(n_type)

    test_ratio = 100 - config["training_ratio"]
    cross_validation_count = 1
    if training_c['cross_validation']:
        training, expected = utils.randomize_data(training, expected)

        if test_ratio != 0:
            if len(training) % int(100 / test_ratio) != 0:
                print("Training set / training ration is not a natural number: " + str(len(training)))
                exit(1)
        else:
            cross_validation_count = int(100 / test_ratio)

    i = 0
    while i < cross_validation_count:
        training_subset, expected_subset, test_training_subset, test_expected_out_subset = utils.subset_data(training,
                                                                                                             expected,
                                                                                                             test_ratio,
                                                                                                             i)

        multi_perceptron = MultilayerPerceptron(fs, system_c["layout"], len(training_subset[0]),
                                                len(expected_subset[0]))

        if 'random' in w_c:
            multi_perceptron.set_w_random(w_c['random'])

        p = len(training_subset)
        j = n = 0

        error = np.inf
        error_min = np.inf

        while error > constants_c['error_threshold'] and j < constants_c['count_threshold']:
            if 'reset_iter' in w_c and (n > p * w_c['reset_iter']):
                multi_perceptron.set_w_random(w_c['random'])
                n = 0

            train_ixs = [random.randint(0, p - 1)]
            for ix in train_ixs:
                multi_perceptron.train(training_subset[ix], expected_subset[ix], constants_c['eta'])

            new_error = multi_perceptron.get_error(training_subset, expected_subset, w_c['error_enhance'])

            error = new_error
            if error < error_min:
                error_min = error

            # TODO: Compute values

            j += 1
            n += 1
        i += 1


if __name__ == '__main__':
    config = parse_config()
    run()
