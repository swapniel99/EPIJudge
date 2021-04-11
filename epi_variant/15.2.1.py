
def n_queens_helper(row, board):
    n = len(board)
    if row == n:
        res = 1
    else:
        res = 0
        for col in range(n):
            if col not in board[:row] and col - row not in [board[i] - i for i in range(row)]\
                    and col + row not in [board[i] + i for i in range(row)]:
                board[row] = col
                res += n_queens_helper(row + 1, board)
    return res


def n_queens(n: int) -> int:
    board = [-1] * n
    return n_queens_helper(0, board)
