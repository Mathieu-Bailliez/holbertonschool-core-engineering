#!/usr/bin/env python3
"""Demonstrate multiple inheritance with a FlyingFish class."""


class Fish:
    "Represents a fish"

    def swin(self):
        """Print how the fish moves."""

        print("The fish is swimming")

    def habitat(self):
        """Print where the fish lives."""

        print("The fish lives in water")


class Bird:
    "Represents a bird"

    def fly(self):
        """Print how the bird moves."""

        print("The bird is flying")

    def habitat(self):
        """Print where the bird lives."""

        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represent a flying fish, inheriting from both Fish and Bird."""

    def fly(self):
        print("The flying fish is soaring!")

    def swin(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
