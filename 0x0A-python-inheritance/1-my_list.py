#!/usr/bin/python3

"""
module which sorts a list of integer

"""


class MyList(list):
    """
    class which inherits from the list class
    contains public instance methods that prints
    the list sorted in ascending order

    """

    

    def print_sorted(self):
        """
        prints the list sorted in ascending order
        returns a new sorted list

        """

        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
