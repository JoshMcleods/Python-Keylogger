def print_board(board):
    print("      1     2     3     ")
    print("   -------------------")
    for i in range(3):
        print(
            f" {i+1} |  {board[i][0]}  |  {board[i][1]}  |  {board[i][2]}  |")
        if i < 2:
            print("   | --------------- |")
    print("   -------------------")


def check_winner(board, player):
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True
        if all(row[i] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False


def is_full(board):
    return all(cell != " " for row in board for cell in row)


board = [[" " for _ in range(3)] for _ in range(3)]

current_player = "X"

while True:
    print_board(board)
    print(f"\nPlayer {current_player}, it's your turn.")

    try:
        row = int(input("Enter row (1-3): ")) - 1
        col = int(input("Enter column (1-3): ")) - 1

        if board[row][col] != " ":
            print("That space is already taken. Try again.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"\n🎉 Player {current_player} wins!")
            break

        if is_full(board):
            print_board(board)
            print("\nIt's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"
    except (ValueError, IndexError):
        print("Invalid input. Please enter numbers between 1 and 3.")
