from typing import List

from test_framework import generic_test

from random import randrange


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:
    start = 0
    end = len(A)

    while start < end:
        rand = randrange(start, end)
        A[rand], A[end - 1] = A[end - 1], A[rand]

        piv = start
        for ptr in range(start, end - 1):
            if A[ptr] < A[end - 1]:
                A[ptr], A[piv] = A[piv], A[ptr]
                piv += 1
        A[piv], A[end - 1] = A[end - 1], A[piv]

        if piv == len(A) - k:
            return A[piv]
        elif piv < len(A) - k:
            start = piv + 1
        else:
            end = piv


if __name__ == '__main__':
    exit(generic_test.generic_test_main('kth_largest_in_array.py', 'kth_largest_in_array.tsv', find_kth_largest))
