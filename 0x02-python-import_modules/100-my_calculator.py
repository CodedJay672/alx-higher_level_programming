#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    l = len (sys.argv)
    if l != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    op = str(sys.argv[2])
    b = int(sys.argv[3])
    if op == "+":
        print("{} {} {} = {}".format(a, op, b, add(a, b)))
    elif op == "-":
        print("{} {} {} = {}".format(a, op, b, sub(a, b)))
    elif op == "*":
        print("{} {} {} = {}".format(a, op, b, mul(a, b)))
    elif op == "/":
        print("{} {} {} = {}".format(a, op, b, div(a, b)))
    else:
        print("Unknown operator: Available operators: +, -, * snd /")
        sys.exit(1)
