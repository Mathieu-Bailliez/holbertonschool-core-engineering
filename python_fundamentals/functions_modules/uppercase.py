#!/usr/bin/env python3
"""Module: Take a string and convert lowercase characters to uppercase using ASCII values."""


def uppercase(str):

    result = ""
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
            letter = ord(letter) - 32
            result = result + chr(letter)
        else:
            result += letter
    print("{}".format(result))
