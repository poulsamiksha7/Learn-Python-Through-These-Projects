def print_board(board):
    for i, row in enumerate(board):
        row_str = ""
        for j, value in enumerate(row):
            row_str += value
            if j != len(row)-1:
                row_str += " | "
        print(row_str)

        if i != len(board)-1:
            print("-----------")


def get_move(turn, board):
    while True:
        try:
            row = int(input("Row (1-3): "))
            col = int(input("Col (1-3): "))
        except ValueError:
            print("Invalid input. Enter numbers.")
            continue

        if row < 1 or row > 3:
            print("Invalid row.")
            continue

        if col < 1 or col > 3:
            print("Invalid column.")
            continue

        if board[row-1][col-1] != " ":
            print("Spot already taken.")
            continue

        break

    board[row-1][col-1] = turn


def computer_move(turn, board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == " ":
                board[row][col] = turn
                return


def check_win(board, turn):
    lines = [
        [(0,0),(0,1),(0,2)],
        [(1,0),(1,1),(1,2)],
        [(2,0),(2,1),(2,2)],
        [(0,0),(1,0),(2,0)],
        [(0,1),(1,1),(2,1)],
        [(0,2),(1,2),(2,2)],
        [(0,0),(1,1),(2,2)],
        [(0,2),(1,1),(2,0)]
    ]

    for line in lines:
        win = True

        for row,col in line:
            if board[row][col] != turn:
                win = False
                break

        if win:
            return True

    return False



player_name = input("Player name: ")

board = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

turn = "X"
turn_number = 0

print_board(board)

while turn_number < 9:

    print()

    if turn == "X":
        print(player_name+"'s turn")
        get_move(turn, board)
    else:
        print("Computer's turn")
        computer_move(turn, board)

    print_board(board)

    if check_win(board, turn):
        break

    if turn == "X":
        turn = "O"
    else:
        turn = "X"

    turn_number += 1


if turn_number == 9:
    print("Tied game")
else:
    if turn=="X":
        print(player_name,"wins! 🎉")
    else:
        print("Computer wins!")