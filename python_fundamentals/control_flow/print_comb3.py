#!/usr/bin/env python3
"""Module : """

for digit1 in range(10):
    for digit2 in range(10):
        if digit1 < digit2:
            print("{}{}".format(digit1, digit2), end="\n" if digit1 == 8 else ", ")
