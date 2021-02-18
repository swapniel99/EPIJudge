from test_framework import generic_test

# n is number of bits.

# # O(n, 1)
# def parity(x: int) -> int:
#     res = 0
#     while x:
#         res ^= x & 1
#         x >>= 1
#     return res


# O(n, 1) in worst case
# def parity(x: int) -> int:
#     res = 0
#     while x:
#         res ^= 1
#         x = x & (x - 1)
#     return res

# # This is a costly operation.
# def bitlength(x):
#     from math import log2, ceil
#     return 1 << ceil(log2(len(bin(x)) - 2))
#
#
# # O(log n, 1)
# def parity(x: int) -> int:
#     if x <= 0xFFFFFFFFFFFFFFFF:
#         bits = 64
#     else:
#         bits = bitlength(x)
#     while bits > 1:
#         bits //= 2
#         x ^= x >> bits
#     return x & 1


# O((n//64) + log(64))
def parity(n):
    x = 0
    bits = 64
    while n:
        x ^= n & 0xFFFFFFFFFFFFFFFF
        n >>= bits
    while bits > 1:
        bits //= 2
        x ^= x >> bits
    return x & 0x1


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
