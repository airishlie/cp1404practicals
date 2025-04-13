"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_sentence(phrase):
    """
    Format a phrase to start with a capital and end with a single full stop.
    >>> format_sentence("hello")
    'Hello.'
    >>> format_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_sentence("welcome!")
    'Welcome!'
    """
    phrase = phrase.strip()
    if not phrase.endswith(".") and not phrase.endswith("!") and not phrase.endswith("?"):
        phrase += "."
    return phrase[0].upper() + phrase[1:]


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should now pass
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    # assert tests to check fuel is set correctly
    car_with_default_fuel = Car()
    assert car_with_default_fuel.fuel == 0, "Default fuel is not 0"

    car_with_fuel = Car(fuel=10)
    assert car_with_fuel.fuel == 10, "Fuel not set correctly when given in constructor"


run_tests()

# Run the doctests
doctest.testmod()


