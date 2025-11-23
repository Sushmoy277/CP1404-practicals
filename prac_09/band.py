class Band:
    """Band class to represent a group of musicians."""

    def __init__(self, name=""):
        """Initialise a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band."""
        musicians_text = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musicians_text})"

    def __repr__(self):
        """Return a string representation for debugging."""
        return str(self)

    def add(self, musician):
        """Add a Musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Make each musician in the band play."""
        for musician in self.musicians:
            print(musician.play())
