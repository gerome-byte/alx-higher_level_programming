#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        a = 0
        b = None
    else:
        a = len(sentence)
        b = sentence[0]
    tuplex = a, b
    return tuplex
