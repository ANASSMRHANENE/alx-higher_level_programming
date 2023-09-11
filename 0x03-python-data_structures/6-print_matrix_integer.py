#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for c in range(len(i)):
            print("{:d}".format(i[c]),
                  end=' ' if c < len(i) - 1 else '')
        print()
