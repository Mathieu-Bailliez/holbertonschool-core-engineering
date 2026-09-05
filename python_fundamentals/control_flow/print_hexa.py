#!/usr/bin/env python3
"""Module : Print numbers from 0 to 98 in decimal and hexadecimal"""

for number in range(99):
    print("{0} = 0x{0:x}".format(number))
