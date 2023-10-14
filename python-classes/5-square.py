#!/usr/bin/python3
class Square:
    """
    Square Class
    
    A class to represent a square.

    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            :obj:`int`: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            :obj:`int`: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square using '#' characters.

        If the size is equal to 0, it prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print('#' * self.__size)
