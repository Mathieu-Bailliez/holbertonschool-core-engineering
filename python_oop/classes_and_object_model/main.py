#!/usr/bin/env python3
"""test file for my 0-square.py"""


Square = __import__("0-square").Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)
