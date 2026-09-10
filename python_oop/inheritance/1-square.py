#!/usr/bin/env python3
"""Create a Square class based on Rectangle class himself based
on BaseGeometry"""


Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Square defined by a private size."""

    def __init__(self, size):
        """Initialize a Square with a validated size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
