import numpy as np

import TP5.perceptron.simple as sp


class ComplexPerceptron:
    def __init__(self,
                 activation_function,
                 activation_function_derived,
                 layout,
                 input_dim,
                 full_hidden=False,
                 momentum=False,
                 mom_alpha=0.9):

        self.network = None
        self.input_dim = input_dim
        self.activation_function = activation_function
        self.activation_function_derived = activation_function_derived
        self.__init_network(layout, full_hidden, momentum, mom_alpha)

    def activation(self, initial_input, training=False):
        activation_values = initial_input
        for layer in self.network:
            activation_values = list(map(lambda s_p: s_p.activation(activation_values, training=training), layer))
            activation_values = np.transpose(np.asarray(activation_values))

        return activation_values

    def retropropagation(self, expected_output, eta, initial_sup_weights, initial_sup_delta):
        sup_weights = initial_sup_weights
        sup_delta = initial_sup_delta
        for layer in reversed(self.network):
            sup_weights, sup_delta = zip(*list(map(
                lambda s_p: s_p.retropropagate(expected_output, sup_weights, sup_delta, eta),
                layer
            )))
            sup_weights = np.asarray(sup_weights)
            sup_delta = np.asarray(sup_delta)

        return sup_weights, sup_delta

    def randomize_weights(self, ref, by_len=False):
        for layer in self.network:
            list(map(lambda s_p: s_p.update_weights(ref, by_len), layer))

    def update_weights(self):
        for layer in self.network:
            list(map(lambda s_p: s_p.update_weights(), layer))

    def __init_network(self, hidden_layout, full_hidden=False, momentum=False, mom_alpha=0.9):
        layout = np.array(hidden_layout, dtype=int)
        self.network = np.empty(shape=len(layout), dtype=np.ndarray)
        for level in range(len(layout)):
            self.network[level] = np.empty(shape=layout[level], dtype=sp.SimplePerceptron)

            dim = layout[level - 1] if level != 0 else self.input_dim

            hidden = full_hidden or level != (len(layout) - 1)
            for index in range(layout[level]):
                self.network[level][index] = sp.SimplePerceptron(self.activation_function, self.activation_function_derived, dim, hidden, index, momentum, mom_alpha)
