#!/usr/bin/env python3
"""Module: Defines a Square class."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square instance with a private instance
        attributes"""

        self.size = size

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def my_print(self):
        """Print the square with the character #"""
        if self.__size == 0:
            print()
        for _ in range(self.size):
            print("#" * self.size)
