import numpy as np


def normalize_data(data: np.ndarray) -> np.ndarray:
    return (2. * (data - np.min(data)) / np.ptp(data) - 1) * 0.9999999999


def randomize_data(training: np.ndarray, expected: np.ndarray) -> (np.ndarray, np.ndarray):
    aux = np.c_[training.reshape(len(training), -1), expected.reshape(len(expected), -1)]
    np.random.shuffle(aux)
    return aux[:, :training.size // len(training)].reshape(training.shape), aux[:,
                                                                            training.size // len(training):].reshape(
        expected.shape)


def subset_data(training: np.ndarray, expected: np.ndarray, ratio: int, cross_validation_count: int) -> (
        np.ndarray, np.ndarray, np.ndarray, np.ndarray):
    length_test = int(len(training) * ratio / 100)

    test_training_data = []
    test_expected_out_data = []

    for i in range(cross_validation_count * length_test, (cross_validation_count + 1) * length_test):
        test_training_data.append(training[i])
        test_expected_out_data.append((expected[i]))

    remove_ixs = np.arange(cross_validation_count * length_test, (cross_validation_count + 1) * length_test)

    training_data = np.delete(training, remove_ixs, 0)
    expected_out_data = np.delete(expected, remove_ixs, 0)

    return training_data, expected_out_data, np.array(test_training_data), np.array(test_expected_out_data)
