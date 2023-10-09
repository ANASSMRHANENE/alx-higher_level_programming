#!/usr/bin/python3
""" 0x0A.  task 12 """


class MyInt(int):
    """Custom int type inverting behavior of != and == operators.

    """

    def __eq__(self, other):
        """Reverses == operator.

        """
        return int(self) != int(other)

    def __ne__(self, other):
        """Reverses != operator.

        """
        return int(self) == int(other)
