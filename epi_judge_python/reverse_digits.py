from test_framework import generic_test


def reverse(x: int) -> int:
    res = 0
    x, sign = abs(x), x / abs(x)
    while x:
        res = res * 10 + x % 10
        x //= 10
    return res * sign


if __name__ == '__main__':
    exit(generic_test.generic_test_main('reverse_digits.py', 'reverse_digits.tsv', reverse))
