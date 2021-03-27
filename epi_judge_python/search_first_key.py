from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    start = 0
    end = len(A)

    while start < end:
        mid = start + (end - start) // 2
        if A[mid] < k:
            start = mid + 1
        else:
            end = mid

    return -1 if start == len(A) or A[start] != k else start


if __name__ == '__main__':
    exit(generic_test.generic_test_main('search_first_key.py', 'search_first_key.tsv', search_first_of_k))
