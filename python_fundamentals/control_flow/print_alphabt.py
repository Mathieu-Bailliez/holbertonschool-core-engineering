#!/usr/bin/env python3

# Define variables
alphabet = ""

# Output info
for i in range(97, 123):
    if chr(i) != 'q' and chr(i) != 'e':
        alphabet += chr(i)
print("{}".format(alphabet), end="\n")
