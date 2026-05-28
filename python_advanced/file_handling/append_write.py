#!/usr/bin/env python3
"""Module append_file"""

def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF-8)\
    and returns the number of characters added"""

    with open(filename, "a", encoding="utf-8") as f:
        nb_character = f.write(text)
        return nb_character
