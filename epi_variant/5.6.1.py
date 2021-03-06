import random


def longest_rep_len(A):
    elem = None
    res = 0
    length = 0
    for a in A:
        if a == elem:
            length += 1
        else:
            elem = a
            res = max(res, length)
            length = 1

    return max(res, length)


def main():
    A = list()

    for i in range(10):
        A.append(random.randrange(3))

    print(A)
    print(longest_rep_len(A))


if __name__ == '__main__':
    main()
