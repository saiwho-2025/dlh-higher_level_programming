#!/usr/bin/python3
"""This module defines a Square."""


class Square:
    """Defines a square by size."""

    def __init__(self, size=0):
        """Initialize the square."""
        self.size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Retrieve the size."""

        return self.__size

    @size.setter
    def size(self, size):
        """Retrieving the size."""

    def area(self):
        """Return the current square area."""
        area = self.__size ** 2
        return area
