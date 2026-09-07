#!/usr/bin/env python3
"""Module: safely divide two integers and handle exceptions"""


def safe_print_division(a, b):
    """Divide a by b, print the result, and return it (or None)."""
    try:
        result = a / b
    except ZeroDivisionError:
        result = a
        return None
    finally:
        print("Inside result: {}".format(result))
    return result
