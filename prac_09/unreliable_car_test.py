"""
CP1404/CP5632 Practical
Test code for UnreliableCar
"""
from unreliable_car import UnreliableCar

def main():
    """Test the UnreliableCar class by simulating driving with high and low reliability."""
    reliable_car = UnreliableCar("Reliable", 100, 90.0)
    unreliable_car = UnreliableCar("Unreliable", 100, 10.0)

    print("Reliable car test (90% reliability):")
    reliable_driven = 0
    for i in range(100):
        reliable_driven += reliable_car.drive(1)
    print(f"Total distance driven: {reliable_driven}km")

    print("\nUnreliable car test (10% reliability):")
    unreliable_driven = 0
    for i in range(100):
        unreliable_driven += unreliable_car.drive(1)
    print(f"Total distance driven: {unreliable_driven}km")

main()
