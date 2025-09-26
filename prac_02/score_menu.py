MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result
(S)how stars
(Q)uit
"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("farewell")


def get_valid_score():
    score = int(input("Enter valid score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter valid score (0-100): "))
    return score


def show_stars(score):
    for i in range(score):
        print('*',  end=' ')
    print()


def print_result(score):
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


main()