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

def game():
    turn = 'X'
    while True:
        printBoard(board)
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
        elif turn == 'O':
            turn = 'X'
        else:
            print('WTF?')
            break

game()
