import numpy as np
import math


def function(x, trust):
    if x >= trust:
        return 1
    if x < -trust:
        return -1
    return 0


def discrete(data: np.ndarray, trust: float, use_trust: bool):
    if not use_trust:
        return data
    return np.vectorize(function)(data, trust)


def get_activation_functions(name: str, beta: float):
    fs = {
        "linear": lambda x: x,
        "tanh": lambda x: np.tanh(x * beta),
        "exp": lambda x: 1 / (1 + math.e ** (-2 * beta * x)),
    }

    # the derived activation func, if it cant be, then return always 1
    act_funcs_der_dict = {
        "linear": lambda x: 1,
        "tanh": lambda x: beta * (1 - (fs["tanh"](x) ** 2)),
        "exp": lambda x: 2 * beta * fs["exp"](x) * (1 - fs["exp"](x))
    }

    return fs[name], act_funcs_der_dict[name]
