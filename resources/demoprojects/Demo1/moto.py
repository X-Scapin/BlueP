import sys
from véhicule import Véhicule

class Moto(Véhicule):
    """ New class Moto"""

    wheel_numbers = 2

    def __init__(self):
        self.name = "moto"
        self.features = list()

    def print_features(self):
        print(self.name + " features :")
        for feature in self.features:
            print("    " + feature[0] + " : " + feature[1])
