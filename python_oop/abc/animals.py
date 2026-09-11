#!/usr/bin/env python3
"""This module defines an abstract Animal hierarchy with specific implementations
for different animal types."""

from abc import ABC, abstractmethod


class Animal(ABC):
     """Abstract base class representing a generic animal"""

     @abstractmethod
     def sound(self):
        """Return the sound made by the animal, must be implemented by the
        subclass"""

class Dog(Animal):
     """Represents a dog, inheriting from Animal."""

     def sound(self):
          """Return the specific bark sound of a dog."""
          return "Bark"

class Cat(Animal):
     """Represents a cat, inheriting from Animal."""

     def sound(self):
          """Return the specific meow sound of a cat."""
          return "Meow"
