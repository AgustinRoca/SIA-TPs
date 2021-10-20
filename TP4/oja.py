import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


def parse_csv(file_path):
    parsed_file = pd.read_csv(file_path)

    countries_list = parsed_file.loc[:, "Country"].values

    properties = parsed_file.iloc[:, 1:8].values
    scaled_properties = StandardScaler().fit_transform(properties)

    return countries_list, scaled_properties


def print_results(pca1, training_set, countries, method):
    countries_pca1 = [np.inner(pca1, training_set[i]) for i in range(len(training_set))]
    print(f'First Primary Component using {method}:')
    print(pca1)
    fig, ax = plt.subplots(1, 1)
    ax.bar(countries, countries_pca1)
    ax.set_ylabel('First Primary Component')
    ax.set_title(f'First Primary Component per country using {method}')
    ax.set_xticks(range(len(countries)))
    ax.set_xticklabels(countries, rotation=90)
    plt.show()


def get_primary_component_with_sklearn(countries, training_set):
    df = pd.read_csv('data/europe.csv')
    cols = ['Area', 'GDP', 'Inflation', 'Life.expect', 'Military', 'Pop.growth', 'Unemployment']
    std_df = StandardScaler().fit_transform(df[cols])
    pca = PCA(n_components=7)
    _ = pca.fit_transform(std_df)[:, 0]
    print_results(pca.components_[0], training_set, countries, 'Sklearn')
    return pca


def get_primary_component_with_oja(eta, training_set, epochs):
    attributes_qty = len(training_set[0])
    weights = np.random.uniform(0, 1, attributes_qty)

    for epoch in range(epochs):
        for aux in training_set:
            s = np.inner(aux, weights)
            weights = weights + eta * s * (aux - np.dot(s, weights))

    norm = np.sqrt(np.inner(weights, weights))
    return weights / norm


def run(eta, epochs):
    (countries, training_set) = parse_csv('data/europe.csv')

    pca = get_primary_component_with_sklearn(countries, training_set)
    pca_2 = get_primary_component_with_oja(eta, training_set, epochs)

    if pca.components_[0][0] * pca_2[0] < 0:
        pca_2 = pca_2 * -1
    print_results(pca_2, training_set, countries, 'Oja')
    print("Diff. between Sklearn and Oja:")
    print(np.abs(np.sum(pca_2 - pca.components_[0])))


if __name__ == '__main__':
    eta = float(sys.argv[1])
    epochs = int(sys.argv[2])
    run(eta, epochs)
