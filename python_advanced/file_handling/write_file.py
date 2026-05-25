#!/usr/bin/env python3


def write_file(filename="", text=""):

    with open(filename, 'w', encoding="utf-8") as f:

        number = f.write(text)
        return number
