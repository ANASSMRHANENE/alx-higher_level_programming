#!/usr/bin/python3
""" 0x0A. task 8 """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits from Rectangle and thus from BaseGeometry

    Args:
        size (int): length of side of square

    Attributes:
        __size (int): length of side of square

    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns square area as size * size.

        * Required by task instructions

        Attributes:
            __size (int): length of side of square

        Returns:
            __size ** 2

        """
        return self.__size ** 2
'''
