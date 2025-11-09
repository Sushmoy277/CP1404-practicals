"""
Estimate: 60 minutes
Actual:   65  minutes

"""

from prac_06.guitar import Guitar


def main():
    """Create a list of guitars from user input and display them."""
    guitars = []
    print("My guitars!")

    name = input("Name: ")
    while name != "":
        year = get_year()
        cost = get_cost()
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        print("These are my guitars:")
        max_length = max(len(guitar.name) for guitar in guitars)  # Find the longest name for alignment
        for i, guitar in enumerate(guitars, 1):
            vintage_string = " (vintage)" if guitar.is_vintage() else ""
            print(
                f"Guitar {i:>1}: {guitar.name:>{max_length}} ({guitar.year}), "
                f"worth ${guitar.cost:>11,.2f}{vintage_string}"
            )


def get_cost():
    while True:
        try:
            cost = float(input("Cost: $"))
            if cost <= 0:
                print("Cost must be a positive number.")
            else:
                return cost
        except ValueError:
            print("Invalid input.")


def get_year():
    """Get a valid year from user input ."""
    while True:
        try:
            year = int(input("Year: "))
            if year <= 0:
                print("Year must be a positive number.")
            else:
                return year
        except ValueError:
            print("Invalid input.")


main()
