#!/usr/bin/python3
"""Rectangle class."""


class Rectangle:
    """Defines a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area calculation."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter calculation."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle using #."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rows = ["#" * self.__width for _ in range(self.__height)]
        return "\n".join(rows)

    def __repr__(self):
        """Return string representation to recreate instance via eval()."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when the instance is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
