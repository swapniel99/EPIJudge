import random
from collections import namedtuple


def false_true(A):
    false = 0
    for ptr in range(len(A)):
        if not A[ptr].key:
            A[ptr], A[false] = A[false], A[ptr]
            false += 1


def main():
    keys = (True, False)

    Obj = namedtuple('Obj', ['key', 'val'])

    A = list()
    for i in range(10):
        t = Obj(random.choice(keys), random.randrange(100))
        A.append(t)
    print(A)
    false_true(A)
    print(A)


if __name__ == '__main__':
    main()
