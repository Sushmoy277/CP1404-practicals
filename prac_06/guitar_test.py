"""
Estimate: 60 minutes
Actual:   40 minutes

"""

from prac_06.guitar import Guitar

def main():
    first = Guitar("Gibson L-5 CES", 1922, 16035.40)
    second = Guitar("Another Guitar", 2013, 15329.91)

    print(f"{first.name} get_age() - Expected {103}. Got {first.get_age()}")
    print(f"{second.name} get_age() - Expected {12}. Got {second.get_age()}")
    print(f"{first.name} is_vintage() - Expected {True}. Got {first.is_vintage()}")
    print(f"{second.name} is_vintage() - Expected {False}. Got {second.is_vintage()}")


main()
