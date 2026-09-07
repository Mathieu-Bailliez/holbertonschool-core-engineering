#!/usr/bin/env python3
"""Module: Safely print an integer and handle invalid values."""


def safe_print_integer(value):
    """Print an integer and return True, or return False for an invalid value."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
