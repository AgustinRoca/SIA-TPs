import numpy as np


class SimplePerceptron(object):

    def __init__(self,
                 activation_function,
                 activation_function_derived,
                 dimension,
                 hidden=False,
                 index=0,
                 momentum=False,
                 momentum_alpha=0.9):

        self.prev_weight_delta = np.zeros(dimension)
        self.momentum = momentum
        self.momentum_alpha = momentum_alpha

        self.index = index
        self.hidden = hidden
        self.weights = np.zeros(dimension)
        self.input = np.zeros(dimension)
        self.activation_function = activation_function
        self.activation_function_derived = activation_function_derived

        self.weights_array = np.zeros(dimension)

    def update_weights(self):
        self.weights += self.weights_array
        if self.momentum:
            self.weights += self.momentum_alpha * self.prev_weight_delta
            self.prev_weight_delta = self.weights_array

    def randomize_weights(self, ref, by_len=False):
        if by_len:
            self.weights = np.random.uniform(
                -np.sqrt(1 / len(self.weights)),
                np.sqrt(1 / len(self.weights)),
                len(self.weights)
            )
        else:
            self.weights = np.random.uniform(-ref, ref, len(self.weights))

    def activation(self, inarray, training=False):
        if training:
            self.input = inarray
        return self.activation_function(np.dot(inarray, self.weights))

    def retropropagate(self, out, sup_weight, sup_delta, eta):
        activation_derived = self.activation_function_derived(np.dot(self.input, self.weights))

        if not self.hidden:
            delta = (out[self.index] - self.activation(self.input)) * activation_derived
        else:
            delta = np.dot(sup_delta, sup_weight[:, self.index]) * activation_derived

        weight_delta = (eta * delta * self.input)
        self.weights_array += weight_delta

        return self.weights, delta
