import sys
from vehicule import Vehicule

class Car(Vehicule):
    """ New class Voiture"""

    wheel_numbers = 4

    def __init__(self, name):
        self.name = name
        self.doors = {}
        self.default_message = "Hello everybody !"

    def print_value(self, sender):
        """DocString : this method print the default value of this instance"""
        print(sender + " say : " + self.default_message)
