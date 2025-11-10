"""
Estimate: 60 minutes
Actual:   20  minutes

"""
CURRENT_YEAR = 2025
VINTAGE_YEAR = 50


class Guitar:
    """Create guitar details with name, year and cost"""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        """Return how old the guitar is in years."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 years or older, False otherwise."""
        return self.get_age() >= VINTAGE_YEAR

    def __lt__(self, other):
        """Return True if this Guitar was made before the other ."""
        return self.year < other.year
