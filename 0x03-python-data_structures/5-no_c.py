#!/usr/bin/python3
def no_c(my_string):
    update_string = ''
    for i in my_string:
        if i != C and i != c:
            update_string += i
    return update_string
