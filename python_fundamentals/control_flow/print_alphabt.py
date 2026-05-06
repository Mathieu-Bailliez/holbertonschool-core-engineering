#!/usr/bin/env python3

# Define variables

# Output info
for index in range(97, 123):
    if index != 101 and index != 113:
        print(chr(index), end="")
    if index >= 123:
        print(" ")