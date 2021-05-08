from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:
    start = 0
    end = len(A) - 1

    while start < end:
        if A[start] < A[end]:
            return start
        mid = start + (end - start) // 2
        if A[mid] < A[start]:
            end = mid
        else:
            start = mid + 1

    return start


if __name__ == '__main__':
    exit(generic_test.generic_test_main('search_shifted_sorted_array.py', 'search_shifted_sorted_array.tsv',
                                        search_smallest))
