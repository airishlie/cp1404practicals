import datetime

class Project:
    """Represent a Project object."""

    def __init__(self, name, start_date, priority, cost_estimate, percent_complete):
        """Initialise a Project instance."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.percent_complete = int(percent_complete)

    def __str__(self):
        """Return string representation of Project."""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, completion: {self.percent_complete}%"

    def __lt__(self, other):
        """Define less than comparison based on priority."""
        return self.priority < other.priority

    def is_complete(self):
        """Determine if the project is complete (100%)."""
        return self.percent_complete >= 100

    def update(self, new_percentage=None, new_priority=None):
        """Update percentage completion and/or priority if provided."""
        if new_percentage is not None:
            self.percent_complete = new_percentage
        if new_priority is not None:
            self.priority = new_priority
