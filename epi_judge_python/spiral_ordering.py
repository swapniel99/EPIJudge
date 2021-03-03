from typing import List

from test_framework import generic_test


def border(square_matrix, depth, res=None):
    N = len(square_matrix)

    if res is None:
        res = list()
    i = depth
    j = depth

    while j < N - depth:
        res.append(square_matrix[i][j])
        j += 1
    j -= 1
    i += 1
    while i < N - depth:
        res.append(square_matrix[i][j])
        i += 1
    i -= 1
    j -= 1
    while j >= depth and i > depth:
        res.append(square_matrix[i][j])
        j -= 1
    j += 1
    i -= 1
    while i >= depth + 1 and j < N - depth - 1:
        res.append(square_matrix[i][j])
        i -= 1

    return res


# def spiral_helper(square_matrix: List[List[int]], depth) -> List[int]:
#     N = len(square_matrix)
#     if depth * 2 >= N:
#         return list()
#     else:
#         return border(square_matrix, depth) + spiral_helper(square_matrix, depth + 1)
#
#
# def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
#     return spiral_helper(square_matrix, 0)


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
