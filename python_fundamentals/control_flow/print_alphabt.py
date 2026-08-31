#!/usr/bin/env python3
"""Module : """


# 2. Alphabet Game (Lowercase)

# Step 1. We loop up to 123 to include 'z' (122)
for leter in range(97, 123):
    # Step 2. We only print if leter is not e or q
    if leter != 101 and leter != 113:
        # Step 3. We control the output using the end parameter
        # and format with :c
        print("{:c}".format(leter), end="\n" if leter == 122 else "")
