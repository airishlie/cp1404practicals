"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MINIMUM_LENGTH = 5
MAXIMUM_LENGTH = 15
IS_SPECIAL_CHARACTER_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MINIMUM_LENGTH} and {MAXIMUM_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    if len(password) < MINIMUM_LENGTH or len(password) > MAXIMUM_LENGTH:
        print(f"Password must between {MINIMUM_LENGTH} and {MAXIMUM_LENGTH}.")
        return False

    number_of_lower = 0
    number_of_upper = 0
    number_of_digit = 0
    number_of_special = 0

    for character in password:
        if character.islower():
            number_of_lower += 1
        elif character.isupper():
            number_of_upper += 1
        elif character.isdigit():
            number_of_digit += 1
        elif character in SPECIAL_CHARACTERS:
            number_of_special += 1
        else :
            pass

    if number_of_lower < 1 or number_of_upper < 1 or number_of_digit < 1:
        return False

    if IS_SPECIAL_CHARACTER_REQUIRED and number_of_special == 0:
        return False
    return True


main()