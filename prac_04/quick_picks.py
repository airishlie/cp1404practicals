# "Quick Pick" Lottery Ticket Generator
import random

NUMBERS_PER_PICK = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45

def main():
    """Get user input and display quick picks"""
    quick_picks = int(input("How many quick picks? "))

    for i in range(quick_picks):
        pick = generate_quick_pick()
        print(" ".join(f"{number:2}" for number in pick))

def generate_quick_pick():
    """Generate a single quick pick with unique random numbers sorted in ascending order"""
    selected_numbers = set()
    while len(selected_numbers) < NUMBERS_PER_PICK:
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        if number not in selected_numbers:
            selected_numbers.add(number)

    return sorted(selected_numbers)


main()