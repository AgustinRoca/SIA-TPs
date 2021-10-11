from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

from TP4.parser import Parser


def tp():
    parser = Parser()
    titles, countries = parser.parse('data/europe.csv')
    attributes_matrix = []
    for country in countries:
        attributes_matrix.append(country.as_array())
    attributes_matrix = StandardScaler().fit_transform(attributes_matrix)
    pca = PCA()
    principal_components = pca.fit_transform(attributes_matrix)

    print('First component')
    for i in range(len(pca.components_[0])):
        print(f"{titles[i]}: {pca.components_[0, i]}")

    print()
    print('Countries')
    ordered_countries = []
    for i in range(len(countries)):
        ordered_countries.append((principal_components[i, 0], countries[i]))
    ordered_countries.sort(reverse=True)
    for i in range(len(ordered_countries)):
        print(f"{ordered_countries[i][1]}: {ordered_countries[i][0]}")


if __name__ == '__main__':
    tp()
