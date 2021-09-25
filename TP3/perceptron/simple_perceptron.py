import numpy as np


class SimplePerceptron:
    def __init__(self, fs, dimension: int, superficial_layer: bool = True, index: int = 0):
        self.index = index
        self.superficial_layer = superficial_layer
        self.fs = fs
        self.w = np.zeros(dimension)
        self.input = np.zeros(dimension)
        self.all_w = np.zeros(dimension)

    """
    :param out is a 1D array used when the perceptron is superficial
    :param sup_w is a 2D matrix with W vectors of superior layer if perceptron is not superficial
    :param sup_d is a 1D array with delta values of superior layer if perceptron is not superficial
    """
    def train(self, eta: float, out: np.ndarray = None, sup_w: np.ndarray = None, sup_delta: np.ndarray = None, epoch: bool = False) -> (np.ndarray, float):
        # Activation
        fp = self.fs['fp'](np.dot(self.input, self.w))

        if self.superficial_layer:
            d_i = np.dot(sup_delta, sup_w[:, self.index]) * fp
        else:
            d_i = (out[self.index] - self.get_activation_value(self.input)) * fp

        delta_w = (eta * d_i * self.input)

        if epoch:
            self.all_w += delta_w
        else:
            self.update_w(delta_w=delta_w)

        return self.w, d_i

    def get_activation_value(self, input_arr: np.ndarray, training: bool = False):
        if training:
            self.input = input_arr
        return self.fs['f'](np.dot(input_arr, self.w))

    def get_error(self, inp: np.ndarray, out: np.ndarray) -> float:
        return np.sum(np.abs((out - self.get_activation_value(inp)) ** 2)) / 2

    def randomize_w(self, ref: float) -> None:
        self.w = np.random.uniform(-ref, ref, len(self.w))

    def update_w(self, delta_w: np.ndarray = np.asarray([]), epoch: bool = False):
        if epoch:
            delta_w = self.all_w
        self.w += delta_w
