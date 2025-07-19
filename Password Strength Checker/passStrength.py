import string


def passwordcheck(password):
    length = len(password) >= 8
    upper = any(c.isupper() for c in password)
    lower = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)
    symbol = any(c in string.punctuation for c in password)

    strength = sum([length, upper, lower, digit, symbol])

    if strength == 5:
        print("You have a strong password")
    elif strength >= 3:
        print("You have a ok password")
    elif strength <= 2:
        print("You have a weak password")

    print("Your passwords strength score is:", strength)


pwd = input("Enter your password:")
strength = passwordcheck(pwd)
