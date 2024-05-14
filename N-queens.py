def is_safe(board, row, col):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col):
    # If all queens are placed
    if col >= len(board):
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_n_queens(board, col + 1):
                return True
            board[i][col] = 0  # Backtrack
    return False

def print_solution(board):
    for row in board:
        print(" ".join(['Q' if x else '.' for x in row]))

def main(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    if solve_n_queens(board, 0):
        print_solution(board)
    else:
        print("No solution exists")

if __name__ == "__main__":
    main(4)  # Solving for 4 queens
