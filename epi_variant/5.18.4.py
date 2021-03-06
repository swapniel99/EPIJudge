

def border(matrix, depth, res=None):
    M = len(matrix)
    N = len(matrix[0])

    if res is None:
        res = list()

    i = depth
    j = depth

    while j < N - depth:
        res.append(matrix[i][j])
        j += 1
    j -= 1
    i += 1
    while i < M - depth:
        res.append(matrix[i][j])
        i += 1
    i -= 1
    j -= 1
    while j >= depth and i > depth:
        res.append(matrix[i][j])
        j -= 1
    j += 1
    i -= 1
    while i >= depth + 1 and j < N - depth - 1:
        res.append(matrix[i][j])
        i -= 1

    return res


def matrix_in_spiral_order(matrix):
    M = len(matrix)
    N = len(matrix[0])
    spiral = list()
    depth = 0
    while depth * 2 < min(M, N):
        border(matrix, depth, spiral)
        depth += 1
    return spiral


def main():
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(matrix_in_spiral_order(matrix))


if __name__ == '__main__':
    main()
