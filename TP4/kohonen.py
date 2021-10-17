import math
import random

import numpy as np


def random_matrix(side, data_dim):
    matrix = []
    for i in range(side):
        matrix.append([])
        for j in range(side):
            matrix[i].append([])
            for k in range(data_dim):
                matrix[i][j].append(random.random())
    return np.array(matrix)


def euclidean_distance(data1, data2):
    return np.linalg.norm(data1 - data2)


class Kohonen:
    def __init__(self, neurons_matrix_side, data):
        self.neurons_matrix_side = neurons_matrix_side
        self.matrix = random_matrix(neurons_matrix_side, len(data[0]))
        self.data = data
        self.t = 1

    def radius(self):
        return 1

    def eta(self):
        return 1/self.t

    def next_step(self):
        random_data = self.data[random.randint(0, len(self.data) - 1)]
        closest_neuron, (row, column) = self.get_closest_to(random_data)
        activated_neurons_indexes = self.get_surrounding_neurons_indexes(row, column)
        for index in activated_neurons_indexes:
            self.matrix[index[0]][index[1]] += self.eta() * (random_data - self.matrix[index[0]][index[1]])
        self.t += 1

    def get_closest_to(self, random_data):
        closest = euclidean_distance(self.matrix[0][0], random_data)
        closest_neuron = self.matrix[0][0]
        closest_position = (0, 0)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                distance = euclidean_distance(self.matrix[i][j], random_data)
                if distance < closest:
                    closest = distance
                    closest_neuron = self.matrix[i][j]
                    closest_position = (i, j)
        return closest_neuron, closest_position

    def get_surrounding_neurons_indexes(self, row, column):
        ans = []
        radius = self.radius()
        for i in range(int(math.floor(row - radius)), int(math.floor(row + radius + 1))):
            if 0 <= i < len(self.matrix):
                for j in range(int(math.floor(column - radius)), int(math.floor(column + radius + 1))):
                    if 0 <= j < len(self.matrix[i]):
                        if euclidean_distance(np.array([i, j]), np.array([row, column])) <= radius:
                            ans.append((i, j))
        return ans

    def get_neighbours(self, row, column):
        ans = []
        radius = 1
        for i in range(int(math.floor(row - radius)), int(math.floor(row + radius + 1))):
            if 0 <= i < len(self.matrix):
                for j in range(int(math.floor(column - radius)), int(math.floor(column + radius + 1))):
                    if 0 <= j < len(self.matrix[i]):
                        if euclidean_distance(np.array([i, j]), np.array([row, column])) <= radius:
                            ans.append((i, j))
        return ans

    def classify(self):
        for step in range(len(self.data) * 500):
            self.next_step()
        classifications = []
        for entry in self.data:
            neuron, classification = self.get_closest_to(entry)
            classifications.append(classification)
        return classifications

    def weight_distance_matrix(self):
        ans = []
        for i, row in enumerate(self.matrix):
            ans.append([])
            for j, neuron in enumerate(row):
                weight_accum = 0
                neighbours = self.get_neighbours(i, j)
                for neighbour_index in neighbours:
                    neighbour = self.matrix[neighbour_index[0]][neighbour_index[1]]
                    weight_accum += euclidean_distance(neuron, neighbour)
                ans[i].append(weight_accum / (len(neighbours) - 1))
        return ans
