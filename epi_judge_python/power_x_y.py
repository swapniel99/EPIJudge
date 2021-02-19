from test_framework import generic_test


def power(x: float, y: int) -> float:
    res = 1.0
    if y < 0:
        y = -y
        x = 1/x
    while y:
        if y & 0x1:
            res *= x
        x *= x
        y >>= 1
    return res


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv', power))
