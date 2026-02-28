WINNING_COMBOS = [
    (0,1,2), (3,4,5), (6,7,8),
    (0,3,6), (1,4,7), (2,5,8),
    (0,4,8), (2,4,6)
]

def print_board(board):
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---+---+---")

def check_winner(board, player):
    return any(board[a] == board[b] == board[c] == player for a, b, c in WINNING_COMBOS)

def get_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, choose a position (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == " ":
                return move
        except ValueError:
            pass
        print("Invalid move. Try again.")

def play_game():
    board = [" "] * 9
    current_player = "X"

    for turn in range(9):
        print_board(board)
        move = get_move(board, current_player)
        board[move] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            return

        current_player = "O" if current_player == "X" else "X"

    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    play_game()