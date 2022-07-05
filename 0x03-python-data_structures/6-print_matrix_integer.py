#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a in range(len(matrix)):
        for b in range(len(matrix[a])):
            print(matrix[a][b], end=' ')
        print()
