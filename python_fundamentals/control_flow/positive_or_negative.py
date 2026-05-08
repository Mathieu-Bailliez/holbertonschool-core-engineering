#!/usr/bin/env python3

# Define variables

number = __import__('random').randint(-10, 10)
negatif = "is negative"
positive = "is positive"
zero = "is zero"

# Output info

if (number > 0):

    print(f"{number} {positive}")

elif (number == 0):

    print(f"{number} {zero}")

else:
    
    print(f"{number} {negatif}")
