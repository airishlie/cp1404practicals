"""CP1404/CP5632 Practical - Guitar Class

Estimate time: 30 minutes
Actual time: 30 minutes (11am - 11.30am)
"""

class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """Return the age of the guitar in years."""
        current_year = 2024  # Update the year if needed
        return current_year - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old, otherwise False."""
        return self.get_age() >= 50

    def __str__(self):
        """Return a string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"
