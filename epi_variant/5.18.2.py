import math


def border_write(square_matrix, depth, P, ctr):
    N = len(square_matrix)

    if depth * 2 + 1 == N:
        square_matrix[depth][depth] = P[ctr]
        ctr += 1
        return ctr

    i = depth
    j = depth

    while j < N - depth - 1:
        square_matrix[i][j] = P[ctr]
        j += 1
        ctr += 1

    while i < N - depth - 1:
        square_matrix[i][j] = P[ctr]
        i += 1
        ctr += 1

    while j > depth:
        square_matrix[i][j] = P[ctr]
        j -= 1
        ctr += 1

    while i > depth:
        square_matrix[i][j] = P[ctr]
        i -= 1
        ctr += 1

    return ctr


def main():
    P = [4, 34, 32, 52, 2, 41, 56, 12, 55]
    d = int(math.sqrt(len(P)))
    sqaure_matrix = [[0] * d for _ in range(d)]
    depth = 0
    ctr = 0
    while 2 * depth < d:
        ctr = border_write(sqaure_matrix, depth, P, ctr)
        depth += 1

    for r in sqaure_matrix:
        print(r)


if __name__ == '__main__':
    main()
