"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Ans: If the numerator and denominator are not integers, and if it's like any words, alphabets etc.
2. When will a ZeroDivisionError occur?
Ans: If we input 0 in the denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Ans:Yes, we can .If we make the code to check if it's a 0 and after detecting if its ,
it will print an error message.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
