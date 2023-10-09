#!/usr/bin/python3
""" 0x0A task 7 """


class BaseGeometry:
    """empty area() method.

    """
    def area(self):
        """only raises exception to notify user.

        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Input filtration for integers

        Args:
            name (str): name bound to object
            value (any): value of object, expecting int

        Exceptions:
            TypeError: if `value` is not an int
            ValueError: if `value` is less than or equal to 0

        """
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
