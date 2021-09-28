import json
import random

import numpy as np
from matplotlib import pyplot as plt

import data_parser
import utils
from TP3.perceptron import activation_functions
from TP3.perceptron.multilayer_perceptron import MultilayerPerceptron
from TP3.plots import plot_multiple_values, plot_values
from TP3.results import compute_results

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
                print("Training set / training ratio is not a natural number: " + str(len(training)))
                exit(1)
        else:
            cross_validation_count = int(100 / test_ratio)

    i = 0
    cross_validation_precision_train = []
    cross_validation_precision_test = []
    cross_validation_error_train = []
    cross_validation_error_test = []
    cross_validation_x = []
    best_results = {}
    while i < cross_validation_count:
        training_subset, expected_subset, test_training_subset, test_expected_subset = utils.subset_data(training,
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

        iterations = []
        errors = []
        precision_test_total = []
        precision_training_total = []
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

            j += 1
            n += 1
            _, best_results = compute_results({}, multi_perceptron, training_subset, expected_subset,
                                              test_training_subset, test_expected_subset, constants_c['delta_results'],
                                              system_c['normalize_output'], system_c['trust_min'])
            precision_training_total.append(best_results["precicion_training"] * 100)
            precision_test_total.append(best_results["precicion_testing"] * 100)
            errors.append(best_results["error_training"])

        best_results, recent_metrics = compute_results(best_results, multi_perceptron, training_subset, expected_subset,
                                                       test_training_subset, test_expected_subset,
                                                       constants_c['delta_results'],
                                                       system_c['normalize_output'], system_c['trust_min'])

        if training_c['cross_validation']:
            cross_validation_x.append(j)
            cross_validation_precision_train.append(recent_metrics['acc_train'] * 100)
            cross_validation_precision_test.append(recent_metrics['acc_test'] * 100)
            cross_validation_error_train.append(recent_metrics['err_train'])
            cross_validation_error_test.append(recent_metrics['err_test'])

        if training_c['cross_validation']:
            plot_values(iterations, "Iteraciones", errors, "Error")
            plot_multiple_values([iterations], "Iteraciones", [precision_training_total], "Precision",
                                 ["Entrenamiento"], min_v=0,
                                 max_v=100)
            plot_multiple_values([range(len(expected)), range(len(expected))],
                                 "Variables independientes",
                                 [expected, multi_perceptron.activation(training)],
                                 "Valor", ["Real", "Predecido"])
        i += 1

    if training_c['cross_validation']:
        plot_multiple_values([cross_validation_x, cross_validation_x], "Iteraciones",
                             [cross_validation_error_train, cross_validation_error_test], "Error",
                             ["Entrenamiento", "Validacion"])
        plot_multiple_values([cross_validation_x, cross_validation_x], "Iteraciones",
                             [cross_validation_precision_train, cross_validation_precision_test], "Precision",
                             ["Entrenamiento", "Validacion"], min_v=0, max_v=100)

    plt.show(block=True)


if __name__ == '__main__':
    config = parse_config()
    run()
