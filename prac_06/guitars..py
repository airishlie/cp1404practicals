"""CP1404/CP5632 Practical - Guitar Program

Estimate time: 15 minutes
Actual time: 25 minutes (11:30am - 11:55am)
"""

from guitar import Guitar

def main():
    """Program to collect and display user's guitars."""
    guitars = []

    print("My guitars!")

    while True:
        name = input("Name: ")
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")

    # Hardcoded test data (comment out user input above for faster testing)
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

main()