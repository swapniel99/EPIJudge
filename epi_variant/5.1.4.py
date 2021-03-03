import random
from collections import namedtuple


def false_true(A):
    true = len(A) - 1
    for ptr in range(len(A) - 1, -1, -1):
        if A[ptr].key:
            A[ptr], A[true] = A[true], A[ptr]
            true -= 1


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
