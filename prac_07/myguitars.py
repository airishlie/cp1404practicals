import csv
from guitar import Guitar


def load_guitars(filename):
    guitars = []
    with open(filename, 'r') as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def display_guitars(guitars):
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, start=1):
        print(f"Guitar {i}: {guitar}")


def add_new_guitars():
    guitars = []
    name = input("Name: ")
    while name != "":
        year = get_valid_int("Year: ")
        cost = get_valid_float("Cost: ")
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
        name = input("Name: ")
    return guitars


def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input; enter a valid number.")


def get_valid_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input; enter a valid number.")


def save_guitars(filename, guitars):
    with open(filename, 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


def main():
    guitars = load_guitars("guitars.csv")
    display_guitars(guitars)

    new_guitars = add_new_guitars()
    guitars.extend(new_guitars)

    guitars.sort()
    print("\nSorted guitars:")
    display_guitars(guitars)

    save_guitars("guitars.csv", guitars)


if __name__ == "__main__":
    main()
