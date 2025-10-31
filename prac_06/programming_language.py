"""
Estimate: 25 minutes
Actual:   32 minutes
"""


class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection="", year=""):
        """Create a ProgrammingLanguage with name, typing , reflection , year."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Returns True/False if the programming language is dynamically typed or not."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Returns a string representation of the programming language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
