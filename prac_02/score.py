"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    result = get_valid_score(score)
    print(result)

    random_score = random.randint(0, 100)
    random_result = get_valid_score(random_score)
    print(f"Random Score: {random_score}, Result: {random_result}")



def get_valid_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return"Excellent"
    elif score >= 50:
        return"Passable"
    else:
        return"Bad"




main()


