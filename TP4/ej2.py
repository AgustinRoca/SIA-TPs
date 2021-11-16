import random

import numpy as np
from matplotlib import pyplot as plt

from hopfield import Hopfield
from TP4.utils.letters import LETTERS_BITS, get_letter_from_bits


def noise_letter(letter, p, preserve_letter):
    letter_bits = LETTERS_BITS[letter.upper()]

    result = [i for row in letter_bits for i in row]
    for i in range(len(result)):
        if p > random.random():
            if result[i] == -1:
                result[i] = 1
            elif not preserve_letter:
                result[i] = -1

    return result


def parse(filename):
    result = []

    with open(filename, 'r') as f:
        chars = f.read()
        letters = 0
        lines_count = 0
        line_c_count = 0

        for i in range(len(chars)):
            c = chars[i]

            if c != '\n':
                if lines_count >= 5:
                    letters += 1
                    lines_count = 0
                    line_c_count = 0

                if c == '*':
                    value = 1
                else:
                    value = -1
                line_c_count += 1
                result = np.append(result, value)
            else:
                lines_count += 1

        letters += 1
    return result.reshape(letters, 5*5)


def plot(letter, y, y2):
    aciertos, = plt.plot(y)
    espureos, = plt.plot(y2)

    aciertos.set_label('Aciertos')
    espureos.set_label('Estados espureos')

    plt.xlabel('Porcentaje de ruido [%]')
    plt.xticks([x for x in range(0, 101, 10)])

    plt.yticks([y for y in range(0, 101, 10)])
    plt.ylabel('Porcentaje [%]')

    plt.legend(bbox_to_anchor=(1, 1))
    plt.title('Aciertos y estados espureos letra {}'.format(letter))

    plt.tight_layout()
    plt.show()


def test(hp, letter, noise):
    test_pattern = noise_letter(letter, noise, True)
    return hp.train_tf(test_pattern, 10, letter, pprint=False)


def run():
    pattern = parse('data/letter_patterns.txt')
    hp = Hopfield(pattern)

    letters = [get_letter_from_bits(l) for l in hp.letter_patterns]
    for c in letters:
        y = []
        y2 = []
        x = []
        for f in range(0, 100):
            v = 0
            sp = 0
            f = f / 100.0
            for _ in range(0, 1000):
                valid, espureo = test(hp, c, f)
                if valid:
                    v += 1
                if espureo:
                    sp += 1

            y.append(v * 100 / 1000)
            y2.append(sp * 100 / 1000)
            x.append(f)
        plot(c, y, y2)


if __name__ == '__main__':
    run()
