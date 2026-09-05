#!/usr/bin/env python3
"""Module: Import a module, add two numbers, and print the result."""


from add_0 import add

if __name__ == "__main__":
    a = 1
    b = 2
    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))
