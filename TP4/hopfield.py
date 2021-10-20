import sys

import numpy as np


class Hopfield:
    def __init__(self, patterns):
        self.letter_patterns = patterns

        self.N = len(patterns[0])
        # Patterns as Columns
        self.ws = np.dot(patterns.T, patterns) / self.N
        np.fill_diagonal(self.ws, 0)

    def update_pattern(self, current_pattern):
        h = np.dot(self.ws, current_pattern)

        aux = np.array([])
        for i in range(len(current_pattern)):
            if h[i] > 0:
                new_value = 1
            if h[i] < 0:
                new_value = -1
            if h[i] == 0:
                new_value = current_pattern[i]
            aux = np.append(aux, new_value)

        return aux

    def get_energy(self, pattern):
        H = 0
        for i in range(self.N):
            for j in range(i + 1, self.N):
                H -= self.ws[i][j] * pattern[i] * pattern[j]
        return H

    def print_letter(self, pattern):
        for i in range(5):
            for j in range(5):
                aux = pattern[i * 5 + j]
                if aux == 1:
                    character = "▓"
                else:
                    character = " "
                sys.stdout.write(character)
            print("")
        return

    def print_state(self, test_pattern, i):
        print("\n*Epoch {} - H={}".format(i, self.get_energy(test_pattern)))
        self.print_letter(test_pattern)

    def train(self, test_pattern, max_iterations):
        i = 0

        self.print_state(test_pattern, i)
        new_pattern = self.update_pattern(test_pattern)
        i += 1
        self.print_state(new_pattern, i)

        while i < 2 or (not np.array_equal(test_pattern, new_pattern) and i <= max_iterations):
            test_pattern = new_pattern
            new_pattern = self.update_pattern(test_pattern)
            i += 1
            self.print_state(new_pattern, i)

        return new_pattern
