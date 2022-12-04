#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    """./100-my_calculator.py a operator b"""
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    c = add(a, b)
    d = sub(a, b)
    e = mul(a, b)
    f = div(a, b)
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if sys.argv[2] == "+":
        print("{:d} + {:d} = {:d}".format(a, b, c))
    elif sys.argv[2] == "-":
        pirint("{:d} - {:d} = {:d}".format(a, b, d))
    elif sys.argv[2] == "*":
        print("{:d} * {:d} = {:d}".format(a, b, e))
    elif sys.argv[2] == "/":
        print("{:d} / {:d} = {:d}".format(a, b, f))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
