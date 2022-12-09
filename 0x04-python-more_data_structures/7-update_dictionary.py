#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        a_dictionary[key] = value
        return a_dictionary
    else:
        updict = {key: value}
        updict.update(a_dictionary)
        return updict
