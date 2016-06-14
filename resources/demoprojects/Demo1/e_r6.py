import sys
from moto import Moto

class ER6(Moto):
    """ New class ER6"""

    def __init__(self, name):
        Moto.__init__(self, name)
        self.features = [('Marque', 'Yamaha'), ('cc', '650')]
        self.er6_model = None