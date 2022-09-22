#!/usr/bin/python3
import sys
if __name__ == "__main__":
    l = len(sys.argv)
    j = 0
    if l == 1:
        print(j)
    else:
        for i in range(1, l):
            j += int(sys.argv[i])
        print("{:d}".format(j))
