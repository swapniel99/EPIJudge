
def get(a, i):
    return int(a[i]) if i in range(0, len(a)) else 0


def bit_string_add(s: str, t:str):
    i = len(s) - 1
    j = len(t) - 1
    carry = 0
    res = list()
    while i >= 0 or j >= 0 or carry > 0:
        temp = get(s, i) + get(t, i) + carry
        res.append('1' if temp & 1 else '0')
        carry = temp >> 1
        i -= 1
        j -= 1

    res.reverse()
    return ''.join(res)


def bit_string_add2(s: str, t:str):
    x, y = int(s, 2), int(t, 2)
    while y:
        x, y = x ^ y, (x & y) << 1
    return bin(x)[2:]


s = '1011'
t = '1101'
print(bit_string_add(s, t))
print(bit_string_add2(s, t))
