import random
from collections import namedtuple


def mauritian_flag(A, keys):
    k1, k2, k3, k4 = keys

    first = 0
    for ptr in range(len(A)):
        if A[ptr].key == k1:
            A[ptr], A[first] = A[first], A[ptr]
            first += 1

    third = len(A) - 1
    ptr = first

    while ptr <= third:
        if A[ptr].key == k2:
            A[ptr], A[first] = A[first], A[ptr]
            first += 1
            ptr += 1
        elif A[ptr].key == k3:
            ptr += 1
        elif A[ptr].key == k4:
            A[ptr], A[third] = A[third], A[ptr]
            third -= 1
        else:
            raise Exception('Invalid key: ', A[ptr].key)


def main():
    keys = ('k1', 'k2', 'k3', 'k4')

    Obj = namedtuple('Obj', ['key', 'val'])

    A = list()
    for i in range(10):
        t = Obj(random.choice(keys), random.randrange(100))
        A.append(t)
    print(A)
    mauritian_flag(A, keys)
    print(A)


if __name__ == '__main__':
    main()
