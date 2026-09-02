#!/usr/bin/env python3
"""Module: """


def print_last_digit(number):

    if number < 0:
        digit = number % -10
    elif number == 0:
        digit = 0
    else:
        digit = number % 10

    print(digit)
    return(digit)
