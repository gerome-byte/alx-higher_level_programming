#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    m = []
    for i in range(len(matrix)):
        z = list(map(lambda x: pow(x, 2), matrix(i)))
        m.append(z)
    return m
