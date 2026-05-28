#!/usr/bin/env python3
"""Module write_file"""

def write_file(filename="", text=""):
    """Write an UTF-8 file and returns the number of characters written"""
    with open(filename, 'w', encoding="utf-8") as f:
        number = f.write(text)
        return number
