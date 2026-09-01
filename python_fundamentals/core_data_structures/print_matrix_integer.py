#!/usr/bin/env python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
    for elem in matrix:
        for i in range(len(elem)):
            if i < len(elem) - 1:
                print("{:d}".format(elem[i]), end=" ")
            else:
                print("{:d}".format(elem[i]))
