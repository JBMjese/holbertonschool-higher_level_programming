#!/usr/bin/python3
"""
Module 10-square
Defines a square and inherits from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square
    """

    def __init__(self, size):
        """
        Initializes a new Square instance

        Args:
            size (int): The size of the square

        Raises:
            ValueError: If size is not a positive integer
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Computes the area of the square

        Returns:
            int: The area
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns the square description

        Returns:
            str: "[Square] <width>/<height>"
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
