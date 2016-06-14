import sys
from car import Car

class Twingo(Car):
    """ New class Twingo"""

    def __init__(self, name):
        Car.__init__(self, name)
        self.twingo_model = None
