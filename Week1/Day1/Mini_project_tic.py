"""
-------------------------------------
TIC TAC TOE
Two Player Command Line Game
-------------------------------------
"""
# Create the game board (2D List) - 3x3 for tic tac toe
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]
print(len(board))


# Display the board
def display_board():
    print("Welcome to TIC TAC TOE!\n")
    print("TIC TAC TOE")
    print("*****************")

    for i, row in enumerate(board):
        print(f"* {row[0]}  |  {row[1]}  |  {row[2]} *")
        if i < len(board) - 1:
            print("* ---| --- | ---*")

    print("*****************")

print(display_board())


# Getting player input
def player_input(player):
    valid = False
    while valid == False:
        row = int(input(f"Player {player}, enter row (1-3): "))
        col = int(input(f"Player {player}, enter column (1-3): "))

        # convert to index (since lists start at 0)
        row = row - 1
        col = col - 1

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid position. Please enter numbers between 1 and 3.")
        elif board[row][col] != " ":
            print("That cell is already taken. Choose another.")
        else:
            valid = True

    return row, col

def check_win(board, player):
    # check rows
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            return True

    # check columns
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True

    # check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    # no win found
    return False


def check_tie(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False  # found an empty cell, so not a tie yet
    return True  # no empty cells found


def play():
    global board
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]

    current_player = "X"
    game_over = False

    while game_over == False:
        display_board()

        row, col = player_input(current_player)
        board[row][col] = current_player

        if check_win(board, current_player):
            display_board()
            print(f"Player {current_player} wins!")
            game_over = True
        elif check_tie(board):
            display_board()
            print("It's a tie!")
            game_over = True
        else:
            # switch player
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"


print(play())

