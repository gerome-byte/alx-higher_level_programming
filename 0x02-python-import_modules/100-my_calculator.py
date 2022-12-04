#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        print(1)
        exit(1)
    if len(sys.argv) - 1 != 3 and len(sys.argv) != 1:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        print(1)
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    c = add(a, b)
    d = sub(a, b)
    e = mul(a, b)
    f = div(a, b)
    if sys.argv[2] == "+":
        print("{:d} + {:d} = {:d}".format(a, b, c))
        print(0)
        exit(0)
    elif sys.argv[2] == "-":
        print("{:d} - {:d} = {:d}".format(a, b, d))
        print(0)
        exit(0)
    elif sys.argv[2] == "*":
        print("{:d} * {:d} = {:d}".format(a, b, e))
        print(0)
        exit(0)
    elif sys.argv[2] == "/":
        print("{:d} / {:d} = {:d}".format(a, b, f))
        print(0)
        exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        print(1)
        exit(1)
