#!/usr/bin/env python3

def read_file(filename=""):
    with open(filename, mode="r", encoding="utf-8") as f:
        content = f.read()
        print(content, end="")


if __name__ == "__main__":
    read_file("my_file_0.txt")
