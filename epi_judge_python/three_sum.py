from typing import List

from test_framework import generic_test


def has_two_sum(A: List[int], t: int, start: int) -> bool:
    end = len(A) - 1

    while start <= end:
        temp = A[start] + A[end]
        if temp == t:
            return True
        elif temp < t:
            start += 1
        else:
            end -= 1

    return False


def has_three_sum(A: List[int], t: int) -> bool:
    A.sort()
    return any(has_two_sum(A, t - A[i], i) for i in range(len(A)))


if __name__ == '__main__':
    exit(generic_test.generic_test_main('three_sum.py', 'three_sum.tsv', has_three_sum))
