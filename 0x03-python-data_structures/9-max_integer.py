#!/usr/bin/python3
def max_integer(my_list=[]):
    my_list.sort()
    x = len(my_list) - 1
    print("{:d}".format(my_list[x]))
