from random import choice

class Tile:

    def __init__(self, x, y, movement):
        self.x = x # X coord of the LEFT half
        self.y = y # Y coord of the TOP half
        self.movement = movement # (x, y)
        self.moved = False

    def move(self):
        self.x += self.movement[0]
        self.y += self.movement[1]

def dist_from_corner(x, y, xy_dim):
    distances = [x + y]
    distances.append((xy_dim - x - 1) + y)
    distances.append(x + (xy_dim - y - 1))
    distances.append((xy_dim - x - 1) + (xy_dim - y - 1))
    return min(distances)

def is_corner(x, y, xy_dim):
    return dist_from_corner(x, y, xy_dim) < (xy_dim // 2) - 1

def print_board(board, xy_dim):
    dir_to_char = {(0, -1): 'U', (0, 1): 'D', (-1, 0): 'L', (1, 0): 'R'}
    print(f'{xy_dim}x{xy_dim} board:')
    for y in range(xy_dim):
        for x in range(xy_dim):
            if is_corner(x, y, xy_dim):
                print('0', end='')
                continue
            tile = board[y][x]
            if tile:
                print(dir_to_char[tile.movement], end='')
            elif x > 0:
                left_tile = board[y][x - 1]
                if left_tile and dir_to_char[left_tile.movement] in ('U', 'D'):
                    print(dir_to_char[left_tile.movement], end='')
                elif y > 0:
                    top_tile = board[y - 1][x]
                    if top_tile and dir_to_char[top_tile.movement] in ('L', 'R'):
                        print(dir_to_char[top_tile.movement], end='')
                    else:
                        print(' ', end='')
                else:
                    print(' ', end='')
            elif y > 0:
                top_tile = board[y - 1][x]
                if top_tile and dir_to_char[top_tile.movement] in ('L', 'R'):
                    print(dir_to_char[top_tile.movement], end='')
                else:
                    print(' ', end='')
            else:
                print(' ', end='')
        print()
    print()

board = []
xy_dim = 0

for i in range(3):
    # Expand the board by 1 tile in all 4 directions
    for j in range(xy_dim):
        board[j].insert(0, None)
        board[j].append(None)
    xy_dim += 2
    board.insert(0, [None] * xy_dim)
    board.append([None] * xy_dim)
    for y in range(xy_dim):
        for x in range(xy_dim):
            tile = board[y][x]
            if tile:
                tile.x += 1
                tile.y += 1
                tile.moved = False
    print_board(board, xy_dim)
    # Find & remove clashing tiles
    for y in range(xy_dim):
        for x in range(xy_dim):
            tile = board[y][x]
            if tile:
                move_x, move_y = tile.movement[0], tile.movement[1]
                if board[tile.y + move_y][tile.x + move_x] and board[tile.y + move_y][tile.x + move_x].movement == (-move_x, -move_y):
                    board[tile.y][tile.x] = None
                    board[tile.y + move_y][tile.x + move_x] = None
    print_board(board, xy_dim)
    # Move all tiles
    for y in range(xy_dim):
        for x in range(xy_dim):
            tile_history = []
            tile = board[y][x]
            tile_history.append(tile)
            if tile and not tile.moved:
                board[y][x] = None
                #print(f'Tile: ({tile.x}, {tile.y}) Board: ({x}, {y})')
                tile.move()
                tile.moved = True
                while board[tile.y][tile.x]:
                    tile = board[tile.y][tile.x]
                    tile_history.append(tile)
                    tile.move()
                    tile.moved = True
                #print(f'Moving ({x}, {y}) ({tile.movement[0]}, {tile.movement[1]})')
                for tile in tile_history:
                    board[tile.y][tile.x] = tile
                #print(f'New location: ({tile.x}, {tile.y})')
    print_board(board, xy_dim)
    # Find empty space & add tiles
    for y in range(xy_dim - 1):
        for x in range(xy_dim - 1):
            if is_corner(x, y, xy_dim) or is_corner(x+1, y, xy_dim) or is_corner(x, y+1, xy_dim) or is_corner(x+1, y+1, xy_dim):
                continue
            # Check if this is the top-left corner of an empty 2x2 space
            # THIS STATEMENT IS WRONG NEEDS TO BE REWRITTEN
            if (not (board[y][x] or board[y+1][x] or board[y][x+1] or board[y+1][x+1])) and ((y == 0 or is_corner(x, y-1, xy_dim) or (board[y-1][x] and board[y-1][x].movement[0] == 0)) or (x == 0 or is_corner(x-1, y, xy_dim) or (board[y][x-1] and board[y][x-1].movement[1] == 0))):
                horizontal = choice([True, False])
                if horizontal:
                    board[y][x] = Tile(x, y, (0, -1))
                    board[y + 1][x] = Tile(x, y + 1, (0, 1))
                    print(f'Created 2 tiles: ({x}, {y}) & ({x}, {y + 1})')
                else:
                    board[y][x] = Tile(x, y, (-1, 0))
                    board[y][x + 1] = Tile(x + 1, y, (1, 0))
                    print(f'Created 2 tiles: ({x}, {y}) & ({x + 1}, {y})')
    # Display the board
    print_board(board, xy_dim)
