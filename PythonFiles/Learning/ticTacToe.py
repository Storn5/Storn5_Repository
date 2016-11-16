board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
         'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
         'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(boardToPrint):
    print('+---+---+---+')
    print('| ' + boardToPrint['top-L'] + ' | ' + boardToPrint['top-M'] + ' | ' + boardToPrint['top-R'] + ' |')
    print('+---+---+---+')
    print('| ' + boardToPrint['mid-L'] + ' | ' + boardToPrint['mid-M'] + ' | ' + boardToPrint['mid-R'] + ' |')
    print('+---+---+---+')
    print('| ' + boardToPrint['low-L'] + ' | ' + boardToPrint['low-M'] + ' | ' + boardToPrint['low-R'] + ' |')
    print('+---+---+---+')

def gameOver():
    boardFull = True
    for i in board:
        if board[i] == ' ':
            boardFull = False
    if boardFull:
        return 'Nobody'
    else:
        #Add win conditions for X here
        #if (board['top-L'] == 'X' and board['top-M'] == 'X' and board['top-R'] == 'X') or
        #(board['mid-L'] == 'X' and board['mid-M'] == 'X' and board['mid-R'] == 'X') or
        #(board['low-L'] == 'X' and board['low-M'] == 'X' and board['low-R'] == 'X') or
        #(board['low-L'] == 'X' and board['mid-L'] == 'X' and board['top-L'] == 'X') or
        #(board['low-M'] == 'X' and board['mid-M'] == 'X' and board['top-M'] == 'X') or
        #(board['low-R'] == 'X' and board['mid-R'] == 'X' and board['top-R'] == 'X') or
        #(board['low-R'] == 'X' and board['mid-M'] == 'X' and board['top-L'] == 'X') or
        #(board['top-R'] == 'X' and board['mid-M'] == 'X' and board['low-L'] == 'X'):
        #    return 'X'
        #Add win conditions for O here
        #elif (board['top-L'] == 'O' and board['top-M'] == 'O' and board['top-R'] == 'O') or
        #(board['mid-L'] == 'O' and board['mid-M'] == 'O' and board['mid-R'] == 'O') or
        #(board['low-L'] == 'O' and board['low-M'] == 'O' and board['low-R'] == 'O') or
        #(board['low-L'] == 'O' and board['mid-L'] == 'O' and board['top-L'] == 'O') or
        #(board['low-M'] == 'O' and board['mid-M'] == 'O' and board['top-M'] == 'O') or
        #(board['low-R'] == 'O' and board['mid-R'] == 'O' and board['top-R'] == 'O') or
        #(board['low-R'] == 'O' and board['mid-M'] == 'O' and board['top-L'] == 'O') or
        #(board['top-R'] == 'O' and board['mid-M'] == 'O' and board['low-L'] == 'O'):
        #    return 'O'
        #else:
        #    return 'notOver'

def game():
    turn = 'X'
    while True:
        printBoard(board)
        if gameOver() != 'notOver':
            print('Game over! ' + gameOver() + ' won!')
            break
        move = input(turn + '\'s move! Where do you want to move? (Enter nothing to quit)\n')
        if move == '':
            break
        elif board[move] == ' ':
            board[move] = turn
        else:
            print('You can\'t move there! Try again!')
            if turn == 'X':
                turn = 'O'
            elif turn == 'O':
                turn = 'X'
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

game()
