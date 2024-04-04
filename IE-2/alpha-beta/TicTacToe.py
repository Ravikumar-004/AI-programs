import math

EMPTY = "-"
PLAYER_X = "X"
PLAYER_O = "O"

def print_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))

def check_winner(board):
    lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], 
            [1, 4, 7], [2, 5, 8],[0, 4, 8], [2, 4, 6]]
    for line in lines:
        if board[line[0]] == board[line[1]] == board[line[2]] != EMPTY:
            return board[line[0]]
    if EMPTY not in board:
        return "tie"
    return None

def evaluate(board):
    winner = check_winner(board)
    if winner == PLAYER_X:
        return 1
    elif winner == PLAYER_O:
        return -1
    else:
        return 0

def AlphaBeta(board, depth, alpha, beta, maximizing_player):
    if check_winner(board) is not None or depth == 0:
        return evaluate(board)

    best_score = -math.inf if maximizing_player else math.inf
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = PLAYER_X if maximizing_player else PLAYER_O
            score = AlphaBeta(board, depth - 1, alpha, beta, not maximizing_player)
            board[i] = EMPTY
            if maximizing_player:
                best_score = max(best_score, score)
                alpha = max(alpha, score)
            else:
                best_score = min(best_score, score)
                beta = min(beta, score)
            if beta <= alpha:
                break
    return best_score

def find_best_move(board):
    best_score = -math.inf
    best_move = None
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = PLAYER_X
            score = AlphaBeta(board, 9, -math.inf, math.inf, False)
            board[i] = EMPTY
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

board = [EMPTY] * 9
while True:
    print_board(board)
    winner = check_winner(board)
    if winner is not None:
        print("Player", winner, "wins!" if winner != "tie" else "It's a tie!")
        break
    if len([cell for cell in board if cell != EMPTY]) % 2 == 0:
        while True:
            move = int(input("Enter O's move (1-9): "))-1
            if board[move] == EMPTY:
                board[move] = PLAYER_O
                break
            else:
                print("Invalid move! Try again.")
    else:
        move = find_best_move(board)
        board[move] = PLAYER_X
