def is_winner(board, player):
    win_conditions = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]],
    ]
    return [player, player, player] in win_conditions

def get_empty_positions(board):
    return [i for i, x in enumerate(board) if x == None]

def minimax(board, depth, is_maximizing, player, opponent):
    if is_winner(board, player):
        return 10 - depth
    elif is_winner(board, opponent):
        return depth - 10
    elif not get_empty_positions(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for position in get_empty_positions(board):
            board[position] = player
            score = minimax(board, depth + 1, False, player, opponent)
            board[position] = None
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for position in get_empty_positions(board):
            board[position] = opponent
            score = minimax(board, depth + 1, True, player, opponent)
            board[position] = None
            best_score = min(best_score, score)
        return best_score

def find_best_move(board, player, opponent):
    best_score = float('-inf')
    best_move = None
    for position in get_empty_positions(board):
        board[position] = player
        score = minimax(board, 0, False, player, opponent)
        board[position] = None
        if score > best_score:
            best_score = score
            best_move = position
    return best_move

# Example board: 0 = X, 1 = O, None = empty
# Board positions:
# 0 | 1 | 2
# 3 | 4 | 5
# 6 | 7 | 8
board = [None, None, None, None, None, None, None, None, None]
player = 'X' # Maximizing player
opponent = 'O' # Minimizing player

move = find_best_move(board, player, opponent)
print(f"Best move for X is at position {move}")
