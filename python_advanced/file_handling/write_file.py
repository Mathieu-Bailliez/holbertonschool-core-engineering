#!/usr/bin/env python3
"""Function that writes a string to a text file (UTF-8) and returns the number
of characters written."""


def write_file(filename="", text=""):
    """Write text to filename and return the number of characters written."""
    with open(filename, "w", encoding="utf-8") as f:
        size = f.write(text)
        return size
