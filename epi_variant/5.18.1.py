

def border_write(square_matrix, depth, ctr):
    N = len(square_matrix)

    if depth * 2 + 1 == N:
        square_matrix[depth][depth] = ctr
        ctr += 1
        return ctr

    i = depth
    j = depth

    while j < N - depth - 1:
        square_matrix[i][j] = ctr
        j += 1
        ctr += 1

    while i < N - depth - 1:
        square_matrix[i][j] = ctr
        i += 1
        ctr += 1

    while j > depth:
        square_matrix[i][j] = ctr
        j -= 1
        ctr += 1

    while i > depth:
        square_matrix[i][j] = ctr
        i -= 1
        ctr += 1

    return ctr


def main():
    d = 4
    sqaure_matrix = [[0] * d for _ in range(d)]
    depth = 0
    ctr = 1
    while 2 * depth < d:
        ctr = border_write(sqaure_matrix, depth, ctr)
        depth += 1

    for r in sqaure_matrix:
        print(r)


if __name__ == '__main__':
    main()
