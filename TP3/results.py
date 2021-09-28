import math

import numpy as np

from TP3.perceptron.multilayer_perceptron import MultilayerPerceptron


def _discrete(data: np.ndarray, trust: float) -> np.ndarray:
    return np.vectorize(lambda x, t: 1 if x > t else (-1 if x < t else 0))(data, trust)


def _accuracy(in_set, expected_out, delta):  # data, expected_out, activation(data), delta(para el rango)
    success = 0
    for data, out in zip(in_set, expected_out):
        if math.isclose(data, out, rel_tol=delta):
            success += 1
    return success / len(in_set)


def _appreciation(train_accuracy, test_accuracy):
    return 0.5 * train_accuracy + 0.5 * test_accuracy


def compute_results(old_results: dict, p: MultilayerPerceptron, training: np.ndarray, expected: np.ndarray,
                    test_training: np.ndarray, test_expected: np.ndarray, d_eq: float, normalize: bool,
                    trust: float) -> (dict, dict):
    if normalize:
        train_predicted = _discrete(p.activation(training), trust)
    else:
        train_predicted = p.activation(training)
    precision_training = _accuracy(train_predicted, expected, d_eq)
    error_training = p.get_error(training, expected)
    appreciation_val = precision_training
    precision_testing = 0
    error_testing = 0
    if len(test_training) != 0:
        if normalize:
            test_predicted = _discrete(p.activation(test_training), trust)
        else:
            test_predicted = p.activation(test_training)
        precision_testing = _accuracy(test_predicted, test_expected, d_eq)
        error_testing = p.get_error(test_training, test_expected)
        appreciation_val = _appreciation(precision_training, precision_testing)

    new_results = {
        "apreciacion": appreciation_val,
        "perceptron": p,

        "precicion_training": precision_training,
        "precicion_testing": precision_testing,

        "error_training": error_training,
        "error_testing": error_testing
    }

    if "apreciacion" in old_results and old_results["apreciacion"] > appreciation_val:
        return old_results, new_results

    return new_results, new_results
