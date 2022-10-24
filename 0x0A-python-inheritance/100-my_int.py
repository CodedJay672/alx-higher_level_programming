#!/usr/bin/python3

"""module which inherits from int"""


class MyInt(int):
    """class that inherits from the int class"""

    def __eq__(self, value):
        """MyInt == method"""

        return self.real != value

    def __ne__(self, value):
        """MyInt != value"""

        return self.real == value
