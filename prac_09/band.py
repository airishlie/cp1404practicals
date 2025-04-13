"""Band class for CP1404 - demonstrates association: Band has Musicians"""


class Band:
    """Band class that stores a list of Musicians."""

    def __init__(self, name=""):
        """Construct a Band with a name and empty musician list."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def __str__(self):
        """Return string showing the band's name and its musicians."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def play(self):
        """Return a string of all musicians playing their first instrument (if any)."""
        return '\n'.join(musician.play() for musician in self.musicians)

