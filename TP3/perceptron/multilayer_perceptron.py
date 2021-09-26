import multiprocessing.pool
import numpy as np

from TP3.perceptron.simple_perceptron import SimplePerceptron


class MultilayerPerceptron:
    def __init__(self, fs, layout: [int], input_dim: int, output_dim: int):
        self.fs = fs
        self._init_network(layout, input_dim, output_dim)

    def train(self, training_set: np.ndarray, expected_out: np.ndarray, eta: float = 0.01):
        self.activation(training_set, training=True)

        superficial_w = np.empty(1)
        superficial_d = np.empty(1)
        for layer in reversed(self.neurons):
            pool = multiprocessing.pool.ThreadPool(processes=len(layer))
            superficial_w, superficial_d = zip(*pool.map(lambda sp: sp.train(expected_out, superficial_w, superficial_d, eta), layer))

            # Tuples to list
            superficial_w = np.asarray(superficial_w)
            superficial_d = np.asarray(superficial_d)

    def activation(self, in_values: np.ndarray, training: bool = False) -> np.ndarray:
        activation_values = in_values
        for layer in self.neurons:
            pool = multiprocessing.pool.ThreadPool(processes=len(layer))
            activation_values = pool.map(lambda sp: sp.get_activation_value(activation_values, training=training), layer)
            activation_values = np.transpose(np.asarray(activation_values))

        return activation_values

    def get_error(self, in_values: np.ndarray, out: np.ndarray, error_enhance: bool = False) -> float:
        if not error_enhance:
            return np.sum(np.abs((out - self.activation(in_values)) ** 2)) / 2

        a = self.activation(in_values)
        return np.sum((1 + out) * np.log(np.divide((1 + out), (1 + a))) / 2 +
                      (1 - out) * np.log(np.divide((1 - out), (1 - a))) / 2)

    def set_w_random(self, ref: float) -> None:
        for layer in self.neurons:
            pool = multiprocessing.pool.ThreadPool(processes=len(layer))
            pool.apply(lambda sp: sp.set_w_random(ref), layer)

    def _init_network(self, hidden_layout: [int], input_dim: int, output_dim: int):
        layout = np.append(np.array(hidden_layout, dtype=int), output_dim)
        self.neurons = np.empty(shape=len(layout), dtype=np.ndarray)

        for level in range(len(layout)):
            self.neurons[level] = np.empty(shape=layout[level], dtype=SimplePerceptron)
            dim = layout[level - 1] if level != 0 else input_dim

            is_last = level == len(layout) - 1

            for index in range(layout[level]):
                self.neurons[level][index] = SimplePerceptron(self.fs, dim, is_last, index)
