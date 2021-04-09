from typing import List

from test_framework import generic_test


def n_queens_helper(row, board, res):
    n = len(board)
    if row == n:
        res.append(list(board))
    else:
        for col in range(n):
            if col not in board[:row] and col - row not in [board[i] - i for i in range(row)]\
                    and col + row not in [board[i] + i for i in range(row)]:
                board[row] = col
                n_queens_helper(row + 1, board, res)


def n_queens(n: int) -> List[List[int]]:
    board = [-1] * n
    res = list()
    n_queens_helper(0, board, res)
    return res


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens, comp))
