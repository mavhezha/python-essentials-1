from random import randrange


def display_board(board):
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print("|", end="")
        for cell in row:
            print(f"   {cell}   |", end="")
        print()
        print("|       |       |       |")
        print("+-------+-------+-------+")


def enter_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid number! Must be between 1 and 9.")
                continue
            row, col = (move - 1) // 3, (move - 1) % 3
            if board[row][col] in ('X', 'O'):
                print("That square is already taken!")
                continue
            board[row][col] = 'O'
            break
        except ValueError:
            print("That's not a number! Try again.")


def make_list_of_free_fields(board):
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ('X', 'O'):
                free.append((row, col))
    return free


def victory_for(board, sign):
    # Check rows
    for row in board:
        if all(cell == sign for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == sign for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == sign for i in range(3)):
        return True
    if all(board[i][2 - i] == sign for i in range(3)):
        return True
    return False


def draw_move(board):
    free = make_list_of_free_fields(board)
    if free:
        row, col = free[randrange(len(free))]
        board[row][col] = 'X'


# --- Build the board with square numbers 1–9 ---
board = []
num = 1
for r in range(3):
    row = []
    for c in range(3):
        row.append(str(num))
        num += 1
    board.append(row)

# Computer's first move: always the center (square 5)
board[1][1] = 'X'
display_board(board)

# --- Main game loop ---
while True:
    # User's turn
    enter_move(board)
    display_board(board)

    if victory_for(board, 'O'):
        print("You won!")
        break

    if not make_list_of_free_fields(board):
        print("It's a tie!")
        break

    # Computer's turn
    draw_move(board)
    display_board(board)

    if victory_for(board, 'X'):
        print("Computer wins!")
        break

    if not make_list_of_free_fields(board):
        print("It's a tie!")
        break