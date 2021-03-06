from typing import List

from test_framework import generic_test


def border(square_matrix, depth, res=None):
    N = len(square_matrix)

    if res is None:
        res = list()

    if N == depth * 2 + 1:
        res.append(square_matrix[depth][depth])
        return res

    i = depth
    j = depth

    while j < N - 1 - depth:
        res.append(square_matrix[i][j])
        j += 1
    while i < N - 1 - depth:
        res.append(square_matrix[i][j])
        i += 1
    while j > depth:
        res.append(square_matrix[i][j])
        j -= 1
    while i > depth:
        res.append(square_matrix[i][j])
        i -= 1

    return res


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    N = len(square_matrix)
    spiral = list()
    depth = 0
    while depth * 2 < N:
        border(square_matrix, depth, spiral)
        depth += 1

    return spiral


if __name__ == '__main__':
    exit(generic_test.generic_test_main('spiral_ordering.py', 'spiral_ordering.tsv', matrix_in_spiral_order))
