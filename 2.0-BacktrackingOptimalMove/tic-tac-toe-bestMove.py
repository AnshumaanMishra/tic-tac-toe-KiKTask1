import random
import time

def getCopy(board):
    board2 = []
    for i in board:
        board2.append(i[::])
    return board2

def getValidMoves(board):
    moves = []
    for i in range(0, 3):
        for j in range(0, 3):
            if(board[i][j] == '.'):
                moves.append((i, j))

    return moves

# Get moves if player wins in the next move
def checkNextMoveWin(board):
    moves = getValidMoves(board)
    for i in moves:
        board2 = getCopy(board)
        board2[i[0]][i[1]] = 'X'
        if(checkWin(board2) == 1):
            return i
    return (-1, -1)

def checkCentreCondition(board):
    if(board[1][1] != 'X'):
        return (-1, -1)
    if(board[0][0] == '.' and (board[0][2] == 'O' or board[2][0] == 'O')):
        return (0, 0)
    elif(board[2][2] == '.' and (board[0][2] == 'O' or board[2][0] == 'O')):
        return (2, 2)
    elif(board[2][0] == '.' and (board[0][0] == 'O' or board[2][2] == 'O')):
        return (2, 0)
    else:
        return (0, 2)


def getBestMove(board, character):
    
    ty, tx = checkCentreCondition(board)
    if(ty != -1 and tx != -1):
        return (ty, tx)

    firstCheck = checkNextMoveWin(board)
    if(firstCheck[0] != -1 and firstCheck[1] != -1):
        return firstCheck
    validMoves = getValidMoves(board)
    # displayBoard(board)
    for i in validMoves:
        # print(i)
        board2 = getCopy(board)
        board2[i[0]][i[1]] = character
        # displayBoard(board2)
        if(checkWin(board2) == -1):
            return i
        newChar = 'X' if character=='O' else 'O'
        ansMove = getBestMove(board2, newChar)
        if(ansMove[0] != -1 and ansMove[1] != -1):
            return ansMove
    return (-1, -1)
    

# Generating Computer Move
def compMove(board):
    x, y = getBestMove(board, 'O')
    if(x == y == -1):
        return getValidMoves(board)[0]

    return (x, y)


# Printing the board
def displayBoard(board):
    print()
    for i in board:
        print("| ", end='')
        for j in i:
            print(f"{j} | ", end='')
        print()
    print()


# Checking for Wins
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
# print("Enter Keys from the numpad in order corresponding to the location of the cross")

# print(getBestMove(board, 'O'))


# Main Loop'

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

