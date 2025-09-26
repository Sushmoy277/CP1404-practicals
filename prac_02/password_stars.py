MINIMUM_LENGTH = 8

password = input("Enter password: ")

while len(password) < MINIMUM_LENGTH:
    print(f"Password must be at least {MINIMUM_LENGTH} characters long.")
    password = input("Enter password: ")

print("*" * len(password))
