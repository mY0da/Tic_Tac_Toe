board = [['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']]

def display_board(board):
    print("      |     |")
    print("  " + board[0][0] + "   |  " + board[0][1] + "  |  " + board[0][2])
    print("______|_____|______")
    print("      |     |")
    print("  " + board[1][0] + "   |  " + board[1][1] + "  |  " + board[1][2])
    print("______|_____|______")
    print("      |     |")
    print("  " + board[2][0] + "   |  " + board[2][1] + "  |  " + board[2][2])
    print("      |     |")

def get_player_move(board, player):
    while True:
        try:
            row = int(input(f"Player {player}, enter row (1-3): ")) - 1
            col = int(input(f"Player {player}, enter column (1-3): ")) - 1

            if 0 <= row <= 2 and 0 <= col <= 2:
                if board[row][col] == '-':
                    return row, col
                else:
                    print("That position is already taken. Try again.")
            else:
                print("Please enter valid row and column numbers (1-3).")
        except ValueError:
            print("Please enter valid row and column numbers (1-3).")

def check_winner(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        # Check rows and columns
        if board[i][0] == board[i][1] == board[i][2] != '-':
            return board[i][0]  # Return the winning symbol
        if board[0][i] == board[1][i] == board[2][i] != '-':
            return board[0][i]  # Return the winning symbol

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != '-':
        return board[0][0]  # Return the winning symbol
    if board[0][2] == board[1][1] == board[2][0] != '-':
        return board[0][2]  # Return the winning symbol

    return None  # Return None if no winner

def check_tie(board):
    # Check for a tie if the board is full
    for row in board:
        if '-' in row:
            return False  # Game not a tie yet
    return True  # Return True if the board is full

def play_game():
    # Initialize the empty board
    board = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]

    current_player = str(input("Choose your weapon (X / O): ")).upper()
    while current_player != "X" and current_player != "O":
        current_player = str(input("Please, choose between X or O: ")).upper()

    game_over = False

    while not game_over:
        # Display the board
        display_board(board)

        # Get the player's move
        row, col = get_player_move(board, current_player)

        # Update the board with the player's move
        board[row][col] = current_player

        # Check for a winner
        winner = check_winner(board)
        if winner:
            display_board(board)
            print(f"Player {winner} wins!")
            game_over = True
            break

        # Check for a tie
        if check_tie(board):
            display_board(board)
            print("It's a tie!")
            game_over = True
            break

        # Switch players
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

    # Ask for a replay or end the game
    replay = input("Do you want to play again? (yes/no): ")
    if replay.lower() == 'yes':
        play_game()
    else:
        print("Thanks for playing!")

# Start the game
if __name__ == '__main__':
    play_game()
