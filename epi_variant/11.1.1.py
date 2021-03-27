import bisect


def first_occurance_greater(A, k):
    start = 0
    end = len(A)

    while start < end:
        mid = start + (end - start) // 2
        if A[mid] <= k:
            start = mid + 1
        else:
            end = mid

    return start


def main():
    A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]

    print(first_occurance_greater(A, 285))
    print(first_occurance_greater(A, -13))
    print(first_occurance_greater(A, 109))


if __name__ == '__main__':
    main()
