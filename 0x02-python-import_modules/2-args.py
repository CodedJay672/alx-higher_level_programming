#!/usr/bin/python3
import sys
if __name__ == "__main__":
    i = len(sys.argv)
    if i == 1:
        print("{:d} arguments.".format(i - 1))
    elif i == 2:
        print("{:d} argument:".format(i - 1))
        for i in range(1, i):
            print("{}: {}".format(i, sys.argv[i]))
    else:
        print("{:d} arguments:".format(i - 1))
        for i in range(1, i):
            print("{}: {}".format(i, sys.argv[i]))
