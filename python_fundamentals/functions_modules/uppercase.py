#!/usr/bin/env python3

def uppercase(str):
    for c in str:
        ascii_value = ord(c)

        if 97 <= ascii_value <= 122:
            print(chr(ascii_value - 32), end="")
        else:
            print(c, end="")

    print()

if __name__ == "__main__":
    uppercase("Holberton")
    uppercase("hello world")
    uppercase("Python123")
    