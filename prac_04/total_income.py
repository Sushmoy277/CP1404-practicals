"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of number_of_months."""
    incomes = []
    is_finished = False
    while not is_finished:
        try:
            number_of_months = int(input("How many number of months? "))
            if number_of_months <= 0:
                print("Number of months must be greater than 0!")
            is_finished = True
        except ValueError:
            print("Please enter valid integer!")

    for month in range(1, number_of_months + 1):
        is_finished = False
        while not is_finished:
            try:
                income = float(input(f"Enter income for month {month}:$ "))
                if income <= 0:
                    print("Income must be greater than 0!")
                incomes.append(income)
                is_finished = True
            except ValueError:
                print("Please enter valid integer!")
    print_report(incomes, number_of_months)


def print_report(incomes, number_of_months: int):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
