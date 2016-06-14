import sys
from vehicule import Vehicule

class Moto(Vehicule):
    """ New class Moto"""

    wheel_numbers = 2

    def __init__(self, name):
        self.name = name
        self.features = list()

    def print_features(self):
        print(self.name + " features :")
        for feature in self.features:
            print("    " + feature[0] + " : " + feature[1])
