import random


# Expression to right propagate rightmost set bit.
def exp1(x):
    return x | (x - 1)


# Expression to get x mod powof2
def exp2(x, powof2):
    return x & (powof2 - 1)


# Expression to test if x is a power of 2
def exp3(x):
    return (x & (x-1)) == 0


def main():
    for i in range(10):
        x = random.randrange(1000)
        print(bin(x), bin(exp1(x)))

    for i in range(10):
        x = random.randrange(1000)
        powof2 = 1 << random.randrange(1, 10)
        print(bin(x), bin(powof2), bin(exp2(x, powof2)), exp2(x, powof2) == x % powof2)

    for i in range(10):
        x = random.randrange(50)
        print(bin(x), exp3(x))


if __name__ == '__main__':
    main()
