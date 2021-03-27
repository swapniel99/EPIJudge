def enclosing_interval(A, k):
    res = [-1, -1]

    start = 0
    end = len(A)
    while start < end:
        mid = start + (end - start) // 2
        if A[mid] < k:
            start = mid + 1
        else:
            end = mid

    if start == len(A) or A[start] != k:
        return res
    else:
        res[0] = start

    end = len(A)
    while start < end:
        mid = start + (end - start) // 2
        if A[mid] <= k:
            start = mid + 1
        else:
            end = mid

    res[1] = end - 1

    return res


def main():
    A = [1, 2, 3, 4, 4, 4, 5, 6, 6, 6, 6, 7, 8]

    print(enclosing_interval(A, 4))


if __name__ == '__main__':
    main()
