#!/usr/bin/python3
def uniq_add(my_list=[]):
    z = list(set(my_list))
    x = 0
    for i in z:
        x += i
    return x
