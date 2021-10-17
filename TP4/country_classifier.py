import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

from kohonen import Kohonen
from parser import Parser


def countries_as_matrix(countries):
    countries_as_arrays = []
    means = []
    stds = []
    for country in countries:
        countries_as_arrays.append(country.as_array())

    for variable in range(len(countries_as_arrays[0])):
        variables = []
        for country in countries_as_arrays:
            variables.append(country[variable])
        means.append(np.mean(variables))
        stds.append(np.std(variables))
        variables = (variables - means[-1])/stds[-1]
        for country, new_val in zip(countries_as_arrays, variables):
            country[variable] = new_val

    return means, stds, countries_as_arrays


def get_matrix_variable(matrix, mean, std, var_index):
    ans = []
    for i, row in enumerate(matrix):
        ans.append([])
        for weight in row:
            ans[i].append(weight[var_index] * std + mean)
    return ans



def classifier():
    k = 5  # TODO: config
    parser = Parser()
    titles, countries = parser.parse('data/europe.csv')
    means, stds, standardized_data = countries_as_matrix(countries)
    kohonen_model = Kohonen(k, standardized_data)
    classifications = kohonen_model.classify()
    for country, classification in zip(countries, classifications):
        print(f"{country.name}: {classification}")

    counter = np.zeros((k, k), dtype=np.int32)
    for classification in classifications:
        counter[classification[0]][classification[1]] += 1

    sns.heatmap(kohonen_model.weight_distance_matrix(), cmap='gray')
    plt.show()
    sns.heatmap(counter, cmap='gray')
    plt.show()
    for var_index in range(len(standardized_data[0])):
        one_var = get_matrix_variable(kohonen_model.matrix, means[var_index], stds[var_index], var_index)
        heat = sns.heatmap(one_var)
        heat.set_title(titles[var_index])
        plt.show()


if __name__ == '__main__':
    classifier()
