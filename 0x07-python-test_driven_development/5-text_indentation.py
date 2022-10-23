#!/usr/bin/python3

"""
function prints a text with 2 lines after ., ? and :
argument is a text containing many characters

"""


def text_indentation(text):
    """
    prints 2 lines after ., ? and :
    takes a text as argument

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    count = 0

    while count < len(text):
        print("{}".format(text[count]), end="")
        if (text[count] == "." or text[count] == "?" or text[count] == ":"):
            print("\n")
            count += 1
        count += 1
