import json


class Config:
    def __init__(self, filename):
        with open(filename) as file:
            config = json.load(file)

        aux = config['task']
        self.exercise = aux['ej']
        self.font_set = aux['fontSet']

        self.epochs = config['epochs']

        self.eta = config['eta']
        self.beta = config['beta']
        self.division_layer = config['divisionLayer']
        self.interval_training = config['interval_training']

        aux = config['momentum']
        self.momentum = aux['enabled']
        self.momentum_factor = aux['factor']

        aux = config['adaptiveLearning']
        self.adaptive_learning = aux['enabled']
        self.adaptive_learning_epochs = aux['epochs']
        self.adaptive_learning_a = aux['a']
        self.adaptive_learning_b = aux['b']
