import sys
from moto import Moto

class Gladius(Moto):
    """ New class Gladius"""

    def __init__(self, name):
        Moto.__init__(self, name)
        self.features = [('Marque', 'Suzuki'), ('cc', '650')]
        self.gladius_model = None