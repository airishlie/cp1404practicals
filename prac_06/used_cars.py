"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    print("Initial car state:", my_car)

    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print("After driving 30 km", my_car)

    # Adding fuel
    my_car.add_fuel(20)
    print ("After adding 20 fuel:", my_car)

    # Driving further than available fuel
    my_car.drive(200)
    print ("After attempting to drive 200 km: ", my_car)

    # Make sure that fuel not negative
    print(f"Final fuel level: {my_car.fuel}")

    # Test __str__()
    print (f"Car string representation: {my_car}")


main()