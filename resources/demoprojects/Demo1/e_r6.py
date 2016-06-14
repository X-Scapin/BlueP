import sys
from moto import Moto

class ER6(Moto):
    """ New class ER6"""

    def __init__(self):
        self.features = [('Marque', 'Yamaha'), ('cc', '650')]
