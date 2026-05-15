#!/usr/bin/env python3

"""
Prints up to x elements from my_list on one line.
Returns the actual number of elements printed.
"""


def safe_print_list(my_list=[], x=0):

    count = 0

    while count < x:
        try:
            print(my_list[count], end="")

            count += 1

        except IndexError:
            break

    print()

    return count
