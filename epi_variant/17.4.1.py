from typing import List


def has_two_sum(A: List[int], t: int, start: int) -> bool:
    end = len(A) - 1

    while start < end:
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
    return any(has_two_sum(A, t - A[i], i + 1) for i in range(len(A)))


a = [5, 2, 3, 4, 3]
t = 13
print(has_three_sum(a, t))
