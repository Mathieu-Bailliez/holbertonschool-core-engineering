#!/usr/bin/env python3

number = __import__('random').randint(-10, 10)
positive = "is positive"
zero = "is zero"
negative = "is negative"

if number > 0:
    print(f"{number} {positive}")
elif number == 0:
    print(f"{number} {zero}")
else:
    print(f"{number} {negative}")

# What blocked me
"""
VS Code automatically changed the single quotes `' '` to double quotes `" "`,
which caused a mismatch with the exact line required by the project.
"""

# What I understood
"""
Be careful with the software you use to avoid copy-paste issues when
transferring code from the instructions to your editor.
"""
