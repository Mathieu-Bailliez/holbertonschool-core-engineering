#!/usr/bin/env python3
"""Module: """


number = __import__('random').randint(-10000, 10000)

if number < 0:
    digit = number % -10
elif number == 0:
    digit = 0
else:
    digit = number % 10

message = f"Last digit of {number} is {digit} and is"

if digit > 5:
    print(f"{message} greater than 5")
elif digit == 0:
    print(f"{message} 0")
else:
    print(f"{message} less than 6 and not 0")



