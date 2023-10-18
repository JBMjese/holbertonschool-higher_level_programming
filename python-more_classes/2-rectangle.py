#!/usr/bin/python3
"""

A module with a Rectangle that does nothing

"""

class Rectangle:
    """
    This class defines a rectangle with width and height.

    Attributes:
        width (:obj:`int`, optional): The width of the rectangle.
        height (:obj:`int`, optional): The height of the rectangle.

    Raises:
        TypeError: If width or height is not an integer.
        ValueError: If width or height is less than 0.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (:obj:`int`, optional): The width of the rectangle.
            height (:obj:`int`, optional): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            :obj:`int`: The width of the rectangle.
        """
