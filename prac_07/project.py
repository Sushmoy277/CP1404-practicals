"""CP1404/CP5632 Practical - Project class"""

DATE_FORMAT = "%d/%m/%Y"


class Project:
    """Represent a simple project."""

    def __init__(self, name, start_date, priority, cost_estimate, completion):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion = completion

    def __lt__(self, other):
        """Allow sorting by priority ."""
        return self.priority < other.priority

    def is_complete(self):
        """Return True if the project is finished."""
        return self.completion >= 100

    def __str__(self):
        """Return a formatted display string."""
        return (f"{self.name}, start: {self.start_date.strftime(DATE_FORMAT)}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, "
                f"completion: {self.completion}%")
