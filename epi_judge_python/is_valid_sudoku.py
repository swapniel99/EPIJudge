from typing import List

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    def is_valid_block(block):
        block = list(filter(lambda x: x > 0, block))
        return len(block) == len(set(block))

    return all(is_valid_block(row) for row in partial_assignment)\
           and all(is_valid_block(partial_assignment[i][j] for i in range(9)) for j in range(9))\
           and all(is_valid_block(partial_assignment[3 * i + i_][3 * j + j_] for i_ in range(3) for j_ in range(3))
                   for i in range(3) for j in range(3))


if __name__ == '__main__':
    exit(generic_test.generic_test_main('is_valid_sudoku.py', 'is_valid_sudoku.tsv', is_valid_sudoku))
