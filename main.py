
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
current_player = "X"
game_over = False
while not game_over:
    print("Game board")
    print("TIC TAC TOE")
    print("****************")
    for row in board:
        print("|" + "|".join(row) + "|")
        print("-------------")
    print("It " + current_player + " turn.")
    row = int(input("Please select row : "))
    col = int(input("Please select  column : "))

    if board[row][col] != " ":
        print("!!Open your Eyes!!")
        continue
    board[row][col] = current_player
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            print(current_player + "WINNER")
            game_over = True
            break
        elif board[0][i] == board[1][i] == board[2][i] != " ":
            print(current_player + " WINNER")
            game_over = True
            break
    if board[0][0] == board[1][1] == board[2][2] != " ":
        print(current_player + " WINNER")
        game_over = True
    elif board[0][2] == board[1][1] == board[2][0] != " ":
        print(current_player + "WINNER")
        game_over = True
    if not any(" " in row for row in board):
        print("It's a tie!")
        game_over = True
    current_player = "0" if current_player == "X" else "X"
