```python
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


# Display the board

def display_board():
    print("Welcome to TIC TAC TOE!\n")

    print("TIC TAC TOE")
    print("*" * 21)

    for i, row in enumerate(board):
        print(f"*  {row[0]}  |  {row[1]}  |  {row[2]}  *")

        if i < len(board) - 1:
            print("* ---|-----|--- *")

    print("*" * 21)


# Getting player input

def player_input(player):

    valid = False

    while valid == False:

        try:
            row = int(input(f"Player {player}, enter row (1-3): "))
            col = int(input(f"Player {player}, enter column (1-3): "))

            # Convert to index
            # because Python lists start at 0
            row = row - 1
            col = col - 1

            # Check if position is within the board
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid position. Please enter numbers between 1 and 3.")

            # Check if cell is already taken
            elif board[row][col] != " ":
                print("That cell is already taken. Choose another.")

            else:
                valid = True

        except ValueError:
            print("Please enter numbers only.")

    return row, col


# Check if a player has won

def check_win(board, player):

    # Check rows
    for row in board:

        if (row[0] == player and
                row[1] == player and
                row[2] == player):

            return True

    # Check columns
    for col in range(3):

        if (board[0][col] == player and
                board[1][col] == player and
                board[2][col] == player):

            return True

    # Check first diagonal
    if (board[0][0] == player and
            board[1][1] == player and
            board[2][2] == player):

        return True

    # Check second diagonal
    if (board[0][2] == player and
            board[1][1] == player and
            board[2][0] == player):

        return True

    # No win found
    return False


# Check if the game is a tie

def check_tie(board):

    for row in board:

        for cell in row:

            if cell == " ":
                return False

    return True


# Main game function

def play():

    current_player = "X"

    game_over = False

    while game_over == False:

        # Display the current board
        display_board()

        # Get player's move
        row, col = player_input(current_player)

        # Place player's symbol
        board[row][col] = current_player

        # Check for a winner
        if check_win(board, current_player):

            display_board()

            print(f"Player {current_player} wins!")

            game_over = True

        # Check for a tie
        elif check_tie(board):

            display_board()

            print("It's a tie!")

            game_over = True

        else:

            # Switch player
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"


# Start the game

play()