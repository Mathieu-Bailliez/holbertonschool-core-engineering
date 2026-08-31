#!/usr/bin/env python3
"""Module: Generate a ramdom number and print if is zero, positive or négative"""


# 0. Positive anything is better than negative nothing

number = __import__("random").randint(-10, 10)

# Spec
"""
Using conditional statements, print:

    <number> is positive if the number is greater than 0
    <number> is zero if the number equals 0
    <number> is negative if the number is less than 0
"""

if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
