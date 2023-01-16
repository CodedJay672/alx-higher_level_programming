#!/usr/bin/python3

"""script that finds the peak value"""


def find_peak(list_of_integers):
    """function that implements the peak
    finder algorithm
    """
    min = 0
    max = len(list_of_integers) - 1

    while min < max:
        mid = min + (max - min + 1)//2
        if (mid - 1 >= 0 and list_of_integers[mid - 1]
                <= list_of_integers[mid]):
            min = mid
        else:
            max = mid - 1
    return list_of_integers[min + 1]
