import sys
from moto import Moto

class Gladius(Moto):
    """ New class Gladius"""

    def __init__(self):
        self.features = [('Marque', 'Suzuki'), ('cc', '650')]
