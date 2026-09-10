#!/usr/bin/env python3
"""Define the BaseGeometry class."""


class BaseGeometry:
    """Represent the base geometry class for all shapes."""

    def area(self):
        """Calculate and return the area of the geometry."""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator(width, width)
        self.integer_validator(height, height)
        self.__width = width
        self.__height = height
