#!/usr/bin/env python3

# Define variables
number = __import__('random').randint(-10, 10)
message_negatif = "is negative"
message_positive = "is positive"
message_zero = "is zero"

# Output info
if (number >= 1):
    print(f"{number} {message_positive}")
elif (number == 0):
    print(f"{number} {message_zero}")
else:
    print(f"{number} {message_negatif}")