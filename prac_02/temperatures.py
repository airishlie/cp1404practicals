MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celcius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celcius = convert_fahrenheit_to_celcius(fahrenheit)
            print(f"Result: {celcius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_fahrenheit_to_celcius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)

def convert_celcius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


main()
