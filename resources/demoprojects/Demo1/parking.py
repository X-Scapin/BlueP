import sys
from twingo import Twingo
from moto import Moto
from e_r6 import ER6
from gladius import Gladius

class Parking():
    """ New class Parking"""

    global_message = "Bienvenu dans votre parking favoris"

    def __init__(self):
        self.vehicules = list()
        self.name = "Vinci"

        twingo = Twingo()
        twingo.owner = "Mark"

        er6 = ER6()
        er6.owner = "Julian"
        er6.name = "er6"
        glad = Gladius()
        glad.owner = "Pierre"
        glad.name = "gladius"

        self.vehicules.append(twingo)
        self.vehicules.append(er6)
        self.vehicules.append(glad)

    def display_vehicules_owner(self):
        """DocString : display the list of vehicules owner"""
        print("List of vehicule owners : ")
        for vehicule in self.vehicules:
            print("    " + vehicule.owner)

    def display_vehicules_features(self):
        for vehicule in self.vehicules:
            if isinstance(vehicule, Moto):
                vehicule.print_features()
            else:
                print("Voiture has different features")

    def print_global_message():
        print(Parking.global_message)
