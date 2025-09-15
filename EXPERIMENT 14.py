import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    for i in range(3):
        if all([spot == player for spot in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def is_board_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def alphabeta(board, depth, alpha, beta, is_maximizing):
    if is_winner(board, "O"):
        return 1
    elif is_winner(board, "X"):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = alphabeta(board, depth + 1, alpha, beta, False)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = alphabeta(board, depth + 1, alpha, beta, True)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
            if beta <= alpha:
                break
        return min_eval

def best_move(board):
    best_score = -math.inf
    move = (-1, -1)
    alpha = -math.inf
    beta = math.inf

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = alphabeta(board, 0, alpha, beta, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]

    while True:
        print_board(board)

        # Player X (human) move
        while True:
            try:
                row = int(input("Enter your move row (0-2): "))
                col = int(input("Enter your move col (0-2): "))
                if row in range(3) and col in range(3) and board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("Invalid move! Try again.")
            except ValueError:
                print("Please enter valid integers.")

        if is_winner(board, "X"):
            print_board(board)
            print("You win!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Computer (O) move
        row, col = best_move(board)
        board[row][col] = "O"
        print(f"Computer places 'O' on ({row}, {col})")

        if is_winner(board, "O"):
            print_board(board)
            print("Computer wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

tic_tac_toe()
