def print_solution(board):
    print("Solution:")
    for row in board:
        print(" ".join(row))
    print()


def is_safe(board, row, col, N):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True


def solve_n_queens_util(board, col, N):
    # Base case: If all queens are placed, then return True
    if col >= N:
        print_solution(board)
        return True

    res = False
    
    # Consider this column and try placing this queen in all rows one by one
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place this queen in board[i][col]
            board[i][col] = 'Q'

            # Make result true if any placement is possible
            res = solve_n_queens_util(board, col + 1, N) or res

            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove queen from board[i][col] (BACKTRACK)
            board[i][col] = '.'
            
    # If the queen cannot be placed in any row in this column col, return False
    return res


def solve_n_queens(N):
    board = [['.' for _ in range(N)] for _ in range(N)]

    if not solve_n_queens_util(board, 0, N):
        print("Solution does not exist")
        return False

    return True


if __name__ == "__main__":
    # Specify the size of board (N x N)
    N = 4
    print(f"Solving {N}-Queen problem:\n")
    solve_n_queens(N)
