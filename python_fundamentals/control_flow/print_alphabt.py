#!/usr/bin/env python3


"""Print the lowercase alphabet except for q and e.

Output must be continuous (no spaces, no new lines
except at end).

You can only use print once in your code """


"""Expected pattern:

abcdfghijklmnoprstuvwxyz
"""

"""Repo:

    GitHub repository: holbertonschool-core-engineering
    Directory: python_fundamentals/control_flow
    File: print_alphabt.py
"""

"""1) How to print alphabet"""

alphabet = ("abcdefghijklmnopqrstuvwxyz\n")

"""2) How to add a new line at end"""

count = 0

for count in alphabet:
    if count != 'e' and count != 'q':
        print(count, end="")


