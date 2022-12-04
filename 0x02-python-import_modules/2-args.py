#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("{:d} argument.".format(len(sys.argv) - 1))
    elif len(sys.argv) == 2:
        print("{:d} argument:".format(len(sys.argv) - 1))
        print("{:d}: {}".format(len(sys.argv) - 1, sys.argv[len(sys.argv) - 1]))
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))
        j = 1
        for i in range(len(sys.argv[1:])):
            print("{:d}: {}".format(j, sys.argv[j]))
            j = j + 1
