def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0

    while True:
        print_board(board)
        player = players[turn % 2]
        row, col = map(int, input(f"Player {player}, enter row and column (1-3): ").split())
        row -= 1
        col -= 1

        if board[row][col] == " ":
            board[row][col] = player

            if check_win(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                break
            elif all(board[i][j] != " " for i in range(3) for j in range(3)):
                print_board(board)
                print("It's a tie!")
                break
            turn += 1
        else:
            print("That position is already taken. Try again.")

if __name__ == "__main__":
    tic_tac_toe()
