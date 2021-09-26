import numpy as np


def parse_files(training_name: str, out_name: str, threshold: int = 1) -> (np.ndarray, np.ndarray, object):
    n_type = int
    try:
        training = np.array(_parse_file(training_name, n_type, threshold, training=True))
    except ValueError:
        n_type = float
        training = np.array(_parse_file(training_name, n_type, threshold, training=True))

    output = np.array(_parse_file(out_name, n_type, threshold, training=False))

    return training, output, n_type


def _parse_file(file_name: str, n_type=float, threshold: int = 1, training: bool = False) -> []:
    training_file = open(file_name, "r")
    data = []

    for line in training_file:
        line_data = [n_type(threshold)] if training else []
        for n in line.split():
            line_data.append(n_type(n))
        data.append(line_data)
    return data
