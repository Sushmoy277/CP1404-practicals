"""
CP1404/CP5632 Practical - Suggested Solution
List exercises
"""


numbers = []
is_finished = False
while not is_finished:
    try:
        for i in range(5):
            number = int(input("Number: "))
            numbers.append(number)
            is_finished = True
    except ValueError:
        print("Please enter a valid number")

print("The first number is", numbers[0])
print("The last number is", numbers[-1])
print("The smallest number is", min(numbers))
print("The largest number is", max(numbers))
print("The average of the numbers is", sum(numbers) / len(numbers))



