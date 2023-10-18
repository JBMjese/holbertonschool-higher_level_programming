#!/usr/bin/python3
"""

A module with a Rectangle that does nothing

"""


class Rectangle:
    """
    A class that represents a rectangle.
    Attributes:
        width: The width of the rectangle.
        height: The height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Constructs a new rectangle.
        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
        """
        self._width = width
        self._height = height
    @property
    def width(self):
        """
        Gets the width of the rectangle.
        Returns:
            The width of the rectangle.
        """
        return self._width
    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.
        Args:
            value: The new width of the rectangle.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value
    @property
    def height(self):
        """
        Gets the height of the rectangle.
        Returns:
            The height of the rectangle.
        """
        return self._height
    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.
        Args:
            value: The new height of the rectangle.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
    def area(self):
        """
        Gets the area of the rectangle.
        Returns:
            The area of the rectangle.
        """
        return self._width * self._height
    def perimeter(self):
        """
        Gets the perimeter of the rectangle.
        Returns:
        """
        