from test_framework import generic_test

chars = '0123456789ABCDEF'
s2d = {c: i for i, c in enumerate(chars)}


# Time O(n + n * (log b1)/(log b2)), Space O(n * (log b1)/(log b2))
def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    start = 0
    neg = False

    if num_as_string[0] == '-':
        neg = True
        start = 1
    elif num_as_string[0] == '+':
        start = 1

    dec = 0
    for i in range(start, len(num_as_string)):
        dec = dec * b1 + s2d[num_as_string[i]]

    if dec == 0:
        return '0'

    res = list()
    while dec:
        res.append(chars[dec % b2])
        dec //= b2

    if neg:
        res.append('-')
    res.reverse()

    return ''.join(res)


if __name__ == '__main__':
    exit(generic_test.generic_test_main('convert_base.py', 'convert_base.tsv', convert_base))
