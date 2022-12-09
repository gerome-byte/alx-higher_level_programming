#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    list1 = []
    for k, v in a_dictionary.items():
        v = v * 2
        list1.append((k, v))
    x = tuple(list1)
    dict2 = dict(x)
    return dict2
