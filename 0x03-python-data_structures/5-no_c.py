#!/usr/bin/env python3
def no_c(my_string):
    in my_string:
        my_string.translate({ord(i): None for i in 'cC'})
        return my_string
