# Tic-Tac-Toe Game
# Human = X
# Computer = O

board = [" " for _ in range(9)]


def display_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()


def check_winner(player):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


def board_full():
    return " " not in board


def computer_move():
    # Computer chooses the first available cell
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            break


print("TIC-TAC-TOE")
print("You are X and Computer is O")
print("Enter positions from 1 to 9")

while True:

    display_board()

    # Human move
    position = int(input("Enter your position (1-9): ")) - 1

    if position < 0 or position > 8 or board[position] != " ":
        print("Invalid move! Try again.")
        continue

    board[position] = "X"

    if check_winner("X"):
        display_board()
        print("You win!")
        break

    if board_full():
        display_board()
        print("Game Draw!")
        break

    # Computer move
    computer_move()

    if check_winner("O"):
        display_board()
        print("Computer wins!")
        break

    if board_full():
        display_board()
        print("Game Draw!")
        break
