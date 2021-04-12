from typing import List


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


def has_k_sum_helper(A: List[int], t: int, k: int, start: int) -> bool:
    if k == 2:
        return has_two_sum(A, t, start)
    else:
        return any(has_k_sum_helper(A, t - A[i], k - 1, i) for i in range(start, len(A)))


def has_k_sum(A: List[int], t: int, k: int) -> bool:
    A.sort()
    return has_k_sum_helper(A, t, k, 0)


a = [5, 2, 3, 4, 3]
t = 10
k = 2
print(has_k_sum(a, sum(a), len(a)))
