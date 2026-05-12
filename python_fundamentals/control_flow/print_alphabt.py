#!/usr/bin/env python3

alphabet = ("abcdefghijklmnopqrstuvwxyz\n")

count = 0

for count in alphabet:
    if count != 'e' and count != 'q':
        print(count, end="")
