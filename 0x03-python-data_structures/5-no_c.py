#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        update_string = ''
        for i in my_string:
            if i != C and i != c:
                update_string += i
        return my_string
