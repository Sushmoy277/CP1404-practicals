"""
CP1404 Practical
UnreliableCar class
"""

import random
from prac_09.car import Car


class UnreliableCar(Car):
    """Car that sometimes does not drive as expected."""

    def __init__(self, name, fuel, reliability):
        """ Initialise an UnreliableCar instance"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """ Attempt to drive the car"""
        random_number = random.uniform(0, 100)
        if random_number < self.reliability:
            # Car is reliable this time – drive as normal
            return super().drive(distance)
        # Car fails to drive this time
        return 0
