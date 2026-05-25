#!/usr/bin/env python3

# a function that reads a text file
# UTF 8 and print it to STDOUT
# USE THE WITH STATEMENT
# NO NEED TO MANAGE FILE PERMISSION
# OR FILE DOEST EXIT EXCEPTIONS
# 0 NOT ALLOWED TO USE IMPORT ANY MODULE

def read_file(filename=""):

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    print(content, end="")


