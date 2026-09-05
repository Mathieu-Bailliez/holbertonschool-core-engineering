#!/usr/bin/env python3
"""Module : Print numbers from 0 to 99 separated by commas."""

for number in range(100):
    print("{0:02}".format(number), end=", " if number < 99 else "\n")
