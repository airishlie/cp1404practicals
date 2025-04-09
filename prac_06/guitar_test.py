"""CP1404/CP5632 Practical - Guitar Class Testing

Estimate time: 10 minutes
Actual time: 8 minutes (12 : 02 pm - 12 : 10 pm)
"""

from guitar import Guitar

def main():
    """Test Guitar class methods."""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 765.40)

    # Test get_age()
    print(f"{gibson.name} get_age() - Expected 102. Got {gibson.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 11. Got {another_guitar.get_age()}")

    # Test is_vintage()
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")

main()
