# Function to check if it's safe to place queen
def is_safe(board, row, col, n):
    # Check same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check left diagonal
    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check right diagonal
    i, j = row-1, col+1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


# Recursive function to solve N-Queens
def solve_nqueens(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve_nqueens(board, row + 1, n):
                return True

            # Backtracking
            board[row][col] = 0

    return False


# Main program
n = int(input("Enter number of queens: "))

board = [[0 for _ in range(n)] for _ in range(n)]

if solve_nqueens(board, 0, n):
    print("Solution:")
    for row in board:
        print(row)
else:
    print("No solution exists")