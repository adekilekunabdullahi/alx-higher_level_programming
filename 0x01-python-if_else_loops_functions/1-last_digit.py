#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
one = "Last digit of"
two = "and is less than 6 and not 0"
# YOUR CODE HERE
if number < 0:
    posnegative = number * -1
    Ldigit = posnegative % 10
    if Ldigit == 0:
        print(f"Last digit of {number} is -{Ldigit} and is 0")
    else:
        print(f"{one} {number} is -{Ldigit} {two}")
else:
    Ldigit = number % 10
    if Ldigit > 5:
        print("Last digit of", number, "is", Ldigit, "and is greater than 5")
    elif Ldigit == 0:
        print("Last digit of", number, "is", Ldigit, "and is 0")
    elif Ldigit < 6 and not 0:
        print(one, number, "is", Ldigit, "and is less than 6 and not 0")
