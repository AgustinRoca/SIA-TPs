import numpy as np


def normalize(data):
    return (2. * (data - np.min(data)) / np.ptp(data) - 1)


def randomize(data, seed):
    aux = np.c_[data.reshape(len(data), -1)]
    if seed != 0:
        np.random.seed(seed)
    np.random.shuffle(aux)
    return aux[:, :data.size // len(data)].reshape(data.shape)


def extract_subset(data, ratio):
    dataset = data
    rest_len = int(len(data) * (1 - ratio))
    rest_data = []

    for i in range(rest_len):
        rest_data.append(data[i])

    return np.delete(dataset, np.arange(0, len(rest_data)), 0), np.array(rest_data)


def generate_noise(data, prob):
    resp = data
    for i in range(1, len(data)):
        if np.random.uniform() < prob:
            resp[i] = 1 - data[i]
    return resp


def generate_noise_dataset(dataset, prob):
    ret = []
    for data in dataset:
        ret.append(generate_noise(data, prob))

    return np.asarray(ret)
