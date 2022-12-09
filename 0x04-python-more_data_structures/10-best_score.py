#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        x = sorted(a_dictionary.values())
        y = list(x)
        z = y[len(y) - 1]
        for k, v in a_dictionary.items():
            if v == z:
                return k
    else:
        return None               
