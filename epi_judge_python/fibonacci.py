from test_framework import generic_test


def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    t0, t1 = 0, 1
    for i in range(2, n + 1):
        t0, t1 = t1, t0 + t1
    return t1


if __name__ == '__main__':
    exit(generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv', fibonacci))
