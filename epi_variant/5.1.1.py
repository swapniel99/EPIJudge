import random
from collections import namedtuple


def dutch_flag(A, keys):
    k1, k2, k3 = keys
    first = 0
    third = len(A) - 1
    ptr = 0

    while ptr <= third:
        if A[ptr].key == k1:
            A[ptr], A[first] = A[first], A[ptr]
            first += 1
            ptr += 1
        elif A[ptr].key == k2:
            ptr += 1
        elif A[ptr].key == k3:
            A[ptr], A[third] = A[third], A[ptr]
            third -= 1
        else:
            raise Exception('Invalid key: ', A[ptr].key)


def main():
    keys = ('k1', 'k2', 'k3')

    Obj = namedtuple('Obj', ['key', 'val'])

    A = list()
    for i in range(10):
        t = Obj(random.choice(keys), random.randrange(100))
        A.append(t)
    print(A)
    dutch_flag(A, keys)
    print(A)


if __name__ == '__main__':
    main()
