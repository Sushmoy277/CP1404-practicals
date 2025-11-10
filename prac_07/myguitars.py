from guitar import Guitar


def main():
    """Read guitars from file, display them, sort them, and display again."""
    guitars = load_guitars("guitars.csv")

    print("These are my guitars:")
    display_guitars(guitars)

    # Sort guitars by year (uses __lt__ from the Guitar class)
    guitars.sort()

    print("\nSorted guitars (oldest to newest):")
    display_guitars(guitars)


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


if __name__ == "__main__":
    main()
