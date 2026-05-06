#!/usr/bin/env python3

# Define variables
number = __import__('random').randint(-10000, 10000)
if number < 0:
    digit = number % -10
else:
    digit = number % 10
message = (f"Last digit of {number} is {digit}")


# Output info
if (digit > 5):
    print(f"{message} and is greater than 5")
elif (digit == 0):
    print(f"{message} and is 0 ")
else:
    print(f"{message} and is less than 6 and not 0")
