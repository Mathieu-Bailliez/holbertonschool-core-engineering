#!/usr/bin/env python3
"""Module: Generate a ramdom number and print if the result  is zero, positive
or négative"""

# Define variables
number = __import__("random").randint(-10, 10)

positive = "is positive"
zero = "is zero"
negative = "is negative"

# Output:
if number > 0:
    print(f"{number} {positive}")
elif number == 0:
    print(f"{number} {zero}")
else:
    print(f"{number} {negative}")
