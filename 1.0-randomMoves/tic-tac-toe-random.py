import random
import time

# Generating Computer Move
def compMove(board):
    mov = random.randint(1, 10)
    y = (9 - mov) // 3
    x = (9 - mov - 1) % 3

    # Check for empty spaces
    while(board[y][x] != '.'):
        mov = random.randint(1, 10)
        y = (9 - mov) // 3
        x = (9 - mov - 1) % 3

    return (y, x)


# Printing the board
def displayBoard(board):
    print()
    for i in board:
        print("| ", end='')
        for j in i:
            print(f"{j} | ", end='')
        print()
    print()


# Checking for wins
def checkWin(board):
    diag1 = board[0][0] if (board[0][0] == board[1][1] == board[2][2] != '.') else '.'
    diag2 = board[0][2] if (board[0][2] == board[1][1] == board[2][0] != '.') else diag1
    row1 = board[0][0] if (board[0][0] == board[0][1] == board[0][2] != '.') else diag2
    col1 = board[0][0] if (board[0][0] == board[1][0] == board[2][0] != '.') else row1
    row2 = board[1][0] if (board[1][0] == board[1][1] == board[1][2] != '.') else col1
    col2 = board[0][1] if (board[0][1] == board[1][1] == board[2][1] != '.') else row2
    row3 = board[2][0] if (board[2][0] == board[2][1] == board[2][2] != '.') else col2
    col3 = board[0][2] if (board[0][2] == board[1][2] == board[2][2] != '.') else row3
    if(col3 == 'X'):
        return 1
    if(col3 == 'O'):
        return -1
    return 0
    
# Initialisation
board = [\
    ['.', '.', '.'], \
    ['.', '.', '.'], \
    ['.', '.', '.']
]
movenum = 0  # To keep track of number of moves and checking tie


displayBoard(board)
print("Enter Keys from the numpad in order corresponding to the location of the cross")

# Main Loop
while(checkWin(board) == 0):
    movenum += 1

    print("Enter Player Move: ")
    inp = int(input())
    
    y = (9 - inp) // 3
    x = 2 - (9 - inp) % 3
    
    if(board[y][x] == '.'):
        board[y][x] = 'X'
    else:
        print("Space already occupied")
        continue
    
    displayBoard(board)
    
    if(checkWin(board) == 1):
        print("Player Wins!!")
        break

    if(movenum == 5 and checkWin(board) == 0):
        print('Tie')
        break

    time.sleep(1)
    
    print("Computer Move: ")

    cy, cx = compMove(board)
    board[cy][cx] = 'O'
    
    displayBoard(board)
    
    if(checkWin(board) == -1):
        print("Computer Wins!!")
        break

