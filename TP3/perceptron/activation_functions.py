import numpy as np
import math


def get_step_activation_function(n_type):
    return {
        'f': lambda x: np.asarray(np.sign(x), n_type),
        'fp': lambda x: 1,
    }


def get_softmax_activation_function(b: float):
    def _softmax(x):
        return 1 / (1 + math.e ** (-2 * b * x))

    def _softmax_p(x):
        f = _softmax(x)
        return 2 * b * f * (1 - f)

    return {
        'f': _softmax,
        'fp': _softmax_p
    }
