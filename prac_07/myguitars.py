from guitar import Guitar


def main():
    """Read guitars from file, display them, sort them, and display again."""
    filename = "guitars.csv"
    guitars = load_guitars("guitars.csv")

    print("These are my guitars:")
    display_guitars(guitars)

    guitars.extend(get_new_guitars())

    # Sort guitars by year
    guitars.sort()

    print("\nSorted guitars (oldest to newest):")
    display_guitars(guitars)
    save_guitars(filename, guitars)


def load_guitars(filename):
    """Read guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            name, year, cost = line.strip().split(",")
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def display_guitars(guitars):
    """Display a list of guitars."""
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")


def get_new_guitars():
    """Ask the user to enter new guitars and return them as a list."""
    guitars = []
    name = input("Enter Your Guitar Name: ")
    while name != "":
        try:
            year = get_year()
            cost = get_cost()
            guitars.append(Guitar(name, year, cost))
        except ValueError:
            print("Invalid input. Please enter valid numbers for year and cost.")
        name = input("Enter Your Guitar Name: ")
    return guitars


def get_year():
    """Get a valid integer year from the user."""
    while True:
        try:
            year = int(input("Year: "))
            return year
        except ValueError:
            print("Invalid input; please enter a valid year.")

def get_cost():
    """Get a valid float cost from the user."""
    while True:
        try:
            cost = float(input("Cost: $"))
            return cost
        except ValueError:
            print("Invalid input; please enter a valid number for cost.")


def save_guitars(filename, guitars):
    """Write all guitars to the CSV file ."""
    with open(filename, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


if __name__ == "__main__":
    main()
