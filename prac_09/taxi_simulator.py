"""
CP1404/CP5632 Practical
Taxi simulator program using Taxi and SilverServiceTaxi classes
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Run the taxi simulator with menu options to choose and drive taxis."""
    taxis = [
        Taxi("Prius", 100, 1.23),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    total_bill = 0.0
    current_taxi = None

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()

    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            for i in range(len(taxis)):
                print(f"{i} - {taxis[i]}")
            try:
                taxi_choice = int(input("Choose taxi: "))
                current_taxi = taxis[taxi_choice]
            except (ValueError, IndexError):
                print("Invalid taxi choice")
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                try:
                    distance = int(input("Drive how far? "))
                    current_taxi.start_fare()
                    current_taxi.drive(distance)
                    fare = current_taxi.get_fare()
                    print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
                    total_bill += fare
                except ValueError:
                    print("Invalid distance")
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    for i in range(len(taxis)):
        print(f"{i} - {taxis[i]}")


main()
