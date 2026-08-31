#!/usr/bin/env python3

number = __import__("random").randint(-10, 10)
positive = "is positive"
zero = "is zero"
negative = "is negative"

if number > 0:
    print(f"{number} {positive}")
elif number == 0:
    print(f"{number} {zero}")
else:
    print(f"{number} {negative}")
