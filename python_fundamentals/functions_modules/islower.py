#!/usr/bin/env python3

def islower(c):
    """
    Returns True if c is a lowercase letter , False otherwise.
    """
    ascii_value = ord(c)

    if ascii_value >= 97 and ascii_value <= 122:
        return True

    return False
