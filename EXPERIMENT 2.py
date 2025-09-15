def print_board(board):
    for row in board:
        print(" ".join("Q" if x else "." for x in row))
    print()

def solve(n, col, diag1, diag2, board):
    row = len(board)
    if row == n:
        print_board(board)
        return True
    for c in range(n):
        if c not in col and (row+c) not in diag1 and (row-c) not in diag2:
            solve(n, col|{c}, diag1|{row+c}, diag2|{row-c}, board+[[c==i for i in range(n)]])
    return False

solve(8, set(), set(), set(), [])
