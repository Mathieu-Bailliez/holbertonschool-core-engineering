#!/usr/bin/env python3
"""Module: """


def print_last_digit(number):

    if number < 0:
        digit = number % -10
    else:
        digit = number % 10

    print(abs(digit))
    return abs(digit)
