"""
CP1404/CP5632 Practical
SilverServiceTaxi class - a specialized Taxi with fanciness and flag fall
"""
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised Taxi with higher fare based on fanciness and flag fall."""
    flag_fall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi with fanciness multiplier."""
        super().__init__(name, fuel, Taxi.price_per_km * fanciness)
        self.fanciness = fanciness

    def get_fare(self):
        """Return the fare including flag fall."""
        return super().get_fare() + self.flag_fall

    def __str__(self):
        """Return a string representation including flagfall info."""
        return f"{super().__str__()} plus flag fall of ${self.flag_fall:.2f}"
