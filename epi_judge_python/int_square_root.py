from test_framework import generic_test


def square_root(k: int) -> int:
    start = 0
    end = k + 1

    while start < end:
        mid = start + (end - start) // 2
        midsq = mid * mid
        if midsq == k:
            return mid
        elif midsq < k:
            start = mid + 1
        else:
            end = mid
    return start - 1


if __name__ == '__main__':
    exit(generic_test.generic_test_main('int_square_root.py', 'int_square_root.tsv', square_root))
