#!/usr/bin/env python3
"""This module demonstrates abstract classes, interfaces,
and duck typing in Python."""


from abc import ABC, abstractmethod

my_pi = 3.141592653589793


class Shape(ABC):
    """Abstract base class representing a geometric shape."""

    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape."""


class Circle(Shape):
    def __init__(self, radius):
        """Initialize the circle with a given radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return my_pi * self.radius ** 2

    def perimeter(self):
        """Calculate the perimeter of the circle."""
        return (2 * my_pi) * self.radius


class Rectangle(Shape):
    """Represents a rectangle shape."""
    def __init__(self, width, height):
        """Initialize the rectangle with a given width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle (width * height)."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle ((width + height) * 2)."""
        return (self.width + self.height) * 2

def shape_info(shape):
    """Print the area and perimeter of any object implementing the shape
    interface."""

    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
