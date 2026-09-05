#!/usr/bin/env python3
"""Module : Print the lowercase alphabet except for the letters e and q"""


# 2. Alphabet Game (Lowercase)

# Step 1. We loop up to 123 to include 'z' (122)
for letter in range(97, 123):
    # Step 2. We only print if letter is not e or q
    if letter != 101 and letter != 113:
        # Step 3. We control the output using the end parameter
        # and format with :c
        print("{:c}".format(letter), end="")
