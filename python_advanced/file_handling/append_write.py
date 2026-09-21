#!/usr/bin/env python3
"""Function that append a string to a text file (UTF-8) and returns the number
of characters written."""


def append_write(filename="", text=""):
    """append text to filename and return the number of characters written."""
    with open(filename, mode="a", encoding="utf-8") as f:
        size = f.write(text)
        return size
