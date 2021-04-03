from random import randrange


def median(A):
    k = len(A) // 2

    start = 0
    end = len(A)

    while start < end:
        rand = randrange(start, end)
        A[rand], A[end - 1] = A[end - 1], A[rand]

        div = start
        for ptr in range(start, end - 1):
            if A[ptr] < A[end - 1]:
                A[ptr], A[div] = A[div], A[ptr]
                div += 1
        A[div], A[end - 1] = A[end - 1], A[div]

        if div == k:
            if len(A) % 2 == 1:
                return A[div]
            else:
                sec = A[0]
                for i in range(1, div):
                    sec = max(sec, A[i])
                return (A[div] + sec) / 2
        elif div < k:
            start = div + 1
        else:
            end = div


def main():
    A = [3, 6, 7, 1, 5, 67, 2, 2]

    print(sorted(A), median(A))


if __name__ == '__main__':
    main()
