from taxi import Taxi

def main():
    my_taxi = Taxi("Prius 1", 100, 1.23)

    # Drive the taxi 40 km
    my_taxi.drive(40)

    # Print taxi details and current fare
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

    my_taxi.start_fare()
    my_taxi.drive(100)

    # Print details and current fare
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")


main()
