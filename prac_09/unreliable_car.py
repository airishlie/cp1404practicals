"""
CP1404/CP5632 Practical
UnreliableCar class that inherits from Car
"""
import random
from car import Car  # assuming car.py is in the same folder


class UnreliableCar(Car):
    """A Car that may not always drive based on its reliability."""
    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar with given reliability."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive the car based on reliability."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        return 0
