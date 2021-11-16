import json

import numpy as np


def parse_config(filename):
    with open(filename, 'r') as f:
        config = json.load(f)
    return config


def parse_file(data_name, threshold = 1):
    number_class = int
    try:
        data = np.array(parse_dataset(data_name, number_class, threshold, training=True))
    except ValueError:
        number_class = float
        data = np.array(parse_dataset(data_name, number_class, threshold, training=True))

    return data, number_class


def parse_dataset(filename, number_class=float, threshold=1, training=False):
    f = open(filename, "r")
    data = []

    for l in f:
        line_data = [number_class(threshold)] if training else []
        for n in l.split():
            line_data.append(number_class(n))
        data.append(line_data)
    return data
