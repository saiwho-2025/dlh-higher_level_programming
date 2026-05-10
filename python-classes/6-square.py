#!/usr/bin/python3
"""This module defines and prints a Square."""


class Square:
    """Defines a square by size and position."""
    def __init__(self, size=0):
        """Initialize the square."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter
    def size(self, size):
        """Retrieving the size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        """Gets the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square."""
        if (
            type(value) is not tuple or
            len(value) != 2 or
            type(value[0]) is not int or
            type(value[1]) is not int or
            value[0] < 0 or
            value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        area = self.__size ** 2
        return area

    def my_print(self):
        """prints in stdout the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.size):
                print("#"*self.size)

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
