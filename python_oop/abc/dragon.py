#!/usr/bin/env python3
"""Module demonstrating mixins with a Dragon that can swim and fly."""


class SwimMixin:
    """Mixin that adds swimming behavior to a class."""

    def swim(self):
        """Print a message indicating the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying behavior to a class."""

    def fly(self):
        """Print a message indicating the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A dragon that gains swimming and flying abilities from mixins."""

    def roar(self):
        """Print a message indicating the dragon roars."""
        print("The dragon roars!")


dragon = Dragon()
dragon.swim()
dragon.fly()
dragon.roar()
