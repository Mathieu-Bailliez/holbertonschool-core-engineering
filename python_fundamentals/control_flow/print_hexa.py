#!/usr/bin/env python3
"""Module : """

for number in range(99):
    # print(f"{number} = 0x{number:x}") # f-string version
    # print("{:d} = 0x{:x}".format(number, number)) # Appeler deux fois la variable
    print("{0} = 0x{0:x}".format(number)) # Utiliser l'index 0 deux fois

