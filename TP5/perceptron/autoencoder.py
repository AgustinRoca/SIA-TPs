import numpy as np
from scipy import optimize

import TP5.extras.functions as f
import TP5.perceptron.complex as cp


class AutoEncoder:
    def __init__(self,
                 activation_function,
                 activation_function_derived,
                 layout,
                 data_dim,
                 latent_dim,
                 momentum=False,
                 mom_alpha=0.9):

        self.data_dim = data_dim
        self.latent_dim = latent_dim
        self.optimizer_error = []

        encoder_layout = layout.copy()
        encoder_layout.append(latent_dim)
        self.encoder = cp.ComplexPerceptron(activation_function, activation_function_derived, encoder_layout,
                                            data_dim, full_hidden=True, momentum=momentum, mom_alpha=mom_alpha)

        decoder_layout = layout[::-1]
        decoder_layout.append(data_dim)
        self.decoder = cp.ComplexPerceptron(activation_function, activation_function_derived, decoder_layout,
                                            latent_dim, full_hidden=False, momentum=momentum, mom_alpha=mom_alpha)

    def train(self, data_in, data_out, eta):
        self.activation(data_in, training=True)
        self.retropropagate(data_out, eta)

    def activation(self, init_input, training=False):
        encoder_out = self.encoder.activation(init_input, training=training)
        return self.decoder.activation(encoder_out, training=training)

    def activation_to_latent_space(self, init_input):
        return self.encoder.activation(init_input, training=False)

    def activation_from_latent_space(self, init_input):
        return self.decoder.activation(init_input, training=False)

    def retropropagate(self, expected_out, eta):
        out_dim = len(expected_out)
        sup_w, sup_delta = self.decoder.retropropagation(expected_out, eta, np.empty(out_dim), np.empty(out_dim))
        return self.encoder.retropropagation(expected_out, eta, sup_w, sup_delta)

    def randomize_weights(self, ref, by_len=False):
        self.encoder.randomize_weights(ref, by_len)
        self.decoder.randomize_weights(ref, by_len)

    def update_weights(self):
        self.encoder.update_weights()
        self.decoder.update_weights()

    def error(self, data_in, data_out, trust, use_trust):
        act = f.discrete(self.activation(data_in)[:, 1:], trust, use_trust)
        out = data_out[:, 1:]
        return (np.linalg.norm(out - act) ** 2) / len(out)

    def flatten_weights(self):
        weights_matrix = []
        for layer in self.encoder.network:
            for s_p in layer:
                weights_matrix.append(s_p.w)
        for layer in self.decoder.network:
            for s_p in layer:
                weights_matrix.append(s_p.w)
        return np.hstack(np.array(weights_matrix, dtype=object))

    def unflatten_weights(self, flat_weights):
        w_index = 0
        for layer in self.encoder.network:
            for s_p in layer:
                s_p.w = flat_weights[w_index:w_index + len(s_p.w)]
                w_index += len(s_p.w)
        for layer in self.decoder.network:
            for s_p in layer:
                s_p.w = flat_weights[w_index:w_index + len(s_p.w)]
                w_index += len(s_p.w)

    def error_minimizer(self, flat_w, data_in, data_out, trust, use_trust):
        self.unflatten_weights(flat_w)
        err = self.error(data_in, data_out, trust, use_trust)
        self.optimizer_error.append(err)
        print(f'Optimizer error: {err}')
        return err

    def train_minimizer(self, data_in, data_out, trust, use_trust, method, max_iter, max_fev):
        flat_weights = self.flatten_weights()
        res = optimize.minimize(self.error_minimizer, flat_weights, method=method,
                                args=(data_in, data_out, trust, use_trust),
                                options={'maxiter': max_iter, 'maxfev': max_fev, 'disp': True})
        self.unflatten_weights(res.x)
        final_err = res.fun
        print(f'Final error is {final_err}')
        return final_err
