from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    if x == 0:
        return '0'

    neg = False
    if x < 0:
        neg = True
        x = -x

    res = list()
    while x:
        res.append(chr(ord('0') + x % 10))
        x //= 10

    if neg:
        res.append('-')

    res.reverse()
    return ''.join(res)


def string_to_int(s: str) -> int:
    start = 0
    neg = False

    if s[0] == '-':
        start = 1
        neg = True
    elif s[0] == '+':
        start = 1

    res = 0
    for i in range(start, len(s)):
        res = 10 * res + ord(s[i]) - ord('0')

    if neg:
        res = -res

    return res


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(generic_test.generic_test_main('string_integer_interconversion.py', 'string_integer_interconversion.tsv',
                                        wrapper))
