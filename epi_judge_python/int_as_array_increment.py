from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    carry = 1
    for i in range(len(A) - 1, -1, -1):
        if carry == 0:
            break
        else:
            temp = A[i] + carry
            A[i] = temp % 10
            carry = temp // 10
    if carry > 0:
        A.append(0)
        A[0] = 1
    return A


if __name__ == '__main__':
    exit(generic_test.generic_test_main('int_as_array_increment.py', 'int_as_array_increment.tsv', plus_one))
