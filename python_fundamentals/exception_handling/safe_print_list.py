#!/usr/bin/env python3
"""Module: Print the first x elements of a list and handle out-of-range
indexes."""


def safe_print_list(my_list=[], x=0):

    nb_print = 0

    try:
        for idx in range(x):
            print(my_list[idx], end="")
            nb_print += 1

    except IndexError:
        pass

    finally:
        print()

    return nb_print
