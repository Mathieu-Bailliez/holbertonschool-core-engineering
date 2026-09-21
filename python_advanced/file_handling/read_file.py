#!/usr/bin/env python3
"""Provide a function that prints the contents of a UTF-8 text file."""


def read_file(filename=""):
    """Read a UTF-8 text file and print its contents to stdout."""
    with open(filename, mode="r", encoding="utf-8") as f:
        content = f.read()
        print(content, end="")
