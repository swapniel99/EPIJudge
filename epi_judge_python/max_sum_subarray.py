from typing import List

from test_framework import generic_test


def find_maximum_subarray(A: List[int]) -> int:
    cum_sum = min_sum = max_sum = 0
    for i in range(len(A)):
        min_sum = min(min_sum, cum_sum)
        cum_sum += A[i]
        max_sum = max(max_sum, cum_sum - min_sum)
    return max_sum


if __name__ == '__main__':
    exit(generic_test.generic_test_main('max_sum_subarray.py', 'max_sum_subarray.tsv', find_maximum_subarray))
