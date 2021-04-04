from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int], n: int) -> None:
    read_A = m - 1
    read_B = n - 1
    write_A = m + n - 1

    while read_A >= 0 and read_B >= 0:
        if B[read_B] > A[read_A]:
            A[write_A] = B[read_B]
            read_B -= 1
        else:
            A[write_A] = A[read_A]
            read_A -= 1
        write_A -= 1

    while read_B >= 0:
        A[write_A] = B[read_B]
        read_B -= 1
        write_A -= 1


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(generic_test.generic_test_main('two_sorted_arrays_merge.py', 'two_sorted_arrays_merge.tsv',
                                        merge_two_sorted_arrays_wrapper))
