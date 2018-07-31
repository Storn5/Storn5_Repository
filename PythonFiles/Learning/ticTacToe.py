board = [' ', ' ', ' ',
         ' ', ' ', ' ',
         ' ', ' ', ' ']

def printBoard():
    print('+---+---+---+')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('+---+---+---+')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('+---+---+---+')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('+---+---+---+')

def gameOver(lastTurn):
    if lastTurn == 'O':
        lastTurn = 'X'
    else:
        lastTurn = 'O'
    boardFull = True
    for i in board:
        if i == ' ':
            boardFull = False
    if (board[0] == board[1] == board[2] != ' ') or (board[3] == board[4] == board[5] != ' ') or (board[6] == board[7] == board[8] != ' ') or (board[0] == board[3] == board[6] != ' ') or (board[1] == board[4] == board[7] != ' ') or (board[2] == board[5] == board[8] != ' ') or (board[0] == board[4] == board[8] != ' ') or (board[2] == board[4] == board[6] != ' '):
        return lastTurn
    elif boardFull:
        return 'Nobody'
    else:
        return 'notOver'

def game():
    turn = 'X'
    while True:
        printBoard()
        if gameOver(turn) != 'notOver':
            print('Game over! ' + gameOver(turn) + ' won!')
            break
        move = input(turn + '\'s turn! Where do you want to move? (Enter nothing to quit)\n')
        if move == '':
            break
        elif board[int(move)] == ' ':
            board[int(move)] = turn
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
