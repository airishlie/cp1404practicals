"""
CP1404/CP5632 Practical
Tests for SilverServiceTaxi
"""

from silver_service_taxi import SilverServiceTaxi


def main():
    # Create a fancy taxi with fanciness of 2
    fancy_taxi = SilverServiceTaxi("Fancy Taxi", 100, 2)

    # Start new fare, drive 18km
    fancy_taxi.start_fare()
    fancy_taxi.drive(18)

    # Check fare calculation
    fare = fancy_taxi.get_fare()
    print(f"Fare: ${fare:.2f}")
    assert round(fare, 2) == 48.78, f"Expected $48.78, but got ${fare:.2f}"


main()
