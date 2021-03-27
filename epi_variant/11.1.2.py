
def get_slope(A, i):
    if i == 0 or (i < len(A) - 1 and A[i] > A[i + 1]):
        return -1
    elif i == len(A) - 1 or (i > 0 and A[i] > A[i - 1]):
        return 1
    else:
        return 0


def local_minima(A):
    start = 0
    end = len(A)

    while start < end:
        mid = start + (end - start) // 2
        slope = get_slope(A, mid)
        if slope == 0:
            return mid
        elif slope < 0:
            start = mid + 1
        elif slope > 0:
            end = mid
    return -1


def main():
    A = [9, 10, 11, 6, 12, 10, 4]
    print(local_minima(A))


if __name__ == '__main__':
    main()
