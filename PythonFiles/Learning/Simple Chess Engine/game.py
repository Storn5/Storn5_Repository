import pygame
import chess
import random

def main():
    #Init pygame
    pygame.init()
    display = pygame.display.set_mode((512, 512))
    pygame.display.set_caption('Simple Chess Engine')
    
    #Load images
    img_board = pygame.image.load('board.png')
    img_pieces = ((pygame.image.load('BP.png'), pygame.image.load('BN.png'), pygame.image.load('BB.png'), pygame.image.load('BR.png'), pygame.image.load('BQ.png'), pygame.image.load('BK.png')),
                  (pygame.image.load('WP.png'), pygame.image.load('WN.png'), pygame.image.load('WB.png'), pygame.image.load('WR.png'), pygame.image.load('WQ.png'), pygame.image.load('WK.png')))
    img_border = pygame.image.load('border.png')
    
    #Init chessboard
    board = chess.Board()
    turn = True
    
    while board.result() == '*':
        #Player's move placeholder
        move, move_piece = '', None
        while turn:
            #Draw board
            display.fill((255, 255, 255))
            display.blit(img_board, (0, 0))
            if len(move) == 2:
                display.blit(img_border, ((ord(move[0])-97)*64, (8-int(move[1]))*64))
            for y in range(8):
                for x in range(8):
                    piece = board.piece_at(chess.square(x, 7-y))
                    if piece:
                        display.blit(img_pieces[piece.color][piece.piece_type-1], (x*64, y*64))
            pygame.display.update()
            
            #Player's move
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    move += chr(97 + (pygame.mouse.get_pos()[0]//64))
                    move += str(8-(pygame.mouse.get_pos()[1]//64))
                    if len(move) == 2:
                        move_piece = board.piece_at(chess.square(pygame.mouse.get_pos()[0]//64, 7-(pygame.mouse.get_pos()[1]//64)))
            if len(move) == 4:
                if move_piece and move_piece.piece_type == 1 and move[3] == '8':
                    move += 'q'
                chessMove = chess.Move.from_uci(move)
                if chessMove in list(board.legal_moves):
                    board.push(chessMove)
                    turn = False
                else:
                    move = ''
        
        if board.result() == '*':
            #Computer's move
            board.push(calculate_move(board))
            turn = True
    print(board.result())
    pygame.quit()

def calculate_move(board):
    moves = {}
    for move in list(board.legal_moves):
        board.push(move)
        #Evaluate position
        opp_moves = {}
        if board.result() == '0-1':
            board.pop()
            return move
        if board.result() == '1/2-1/2':
            moves[move] = 0
            board.pop()
            continue
        for opp_move in list(board.legal_moves):
            eval = 0
            board.push(opp_move)
            if board.result() == '1-0':
                opp_moves[opp_move] = -999
                board.pop()
                break
            if board.result() == '1/2-1/2':
                opp_moves[opp_move] = 0
                board.pop()
                continue
            for y in range(8):
                for x in range(8):
                    piece = board.piece_at(chess.square(x, 7-y))
                    if piece:
                        if piece.piece_type == 1:
                            piece_price = 1
                        elif piece.piece_type == 2:
                            piece_price = 3
                        elif piece.piece_type == 3:
                            piece_price = 3
                        elif piece.piece_type == 4:
                            piece_price = 5
                        elif piece.piece_type == 5:
                            piece_price = 9
                        else:
                            piece_price = 0
                        if piece.color:
                            piece_price *= -1
                        eval += piece_price
                    opp_moves[opp_move] = eval
            board.pop()
        best_opp_move = min(opp_moves, key = opp_moves.get)
        moves[move] = opp_moves[best_opp_move]
        board.pop()
        print('Calculated ' + str(move))
    best_move = max(moves, key = moves.get)
    best_moves = []
    for move in moves:
        if moves[move] == moves[best_move]:
            best_moves.append(move)
    print('Eval: ' + str(moves[best_move]))
    return random.choice(best_moves)

if __name__ == '__main__':
    main()