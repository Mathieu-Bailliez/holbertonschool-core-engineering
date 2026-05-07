#!/usr/bin/env python

def uppercase(str):
    for c in str:
        if 97 <= ord(c) <= 122:
            print(chr(ord(c) - 32), end="")
        else:
            print(c, end="")
    print()
