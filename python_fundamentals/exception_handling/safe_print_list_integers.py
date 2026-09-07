#!/usr/bin/env python3
"""Module: safe print first x element of a list and handle exceptions"""


def safe_print_list_integers(my_list=[], x=0):
    """Display the first x elements of my_list that are integers.Return the
    number of integers displayed
    """
    count = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return count
