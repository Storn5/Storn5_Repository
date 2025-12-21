import math
import pygame
from pygame.locals import *

player_width = 50
player_height = 100
player_x = 300
player_y = 600 - player_height
player_grounded = True
player_moving = False
player_x_speed = 0
player_y_speed = 0
won = False

class Box:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.color_timeout = 0

box1 = Box(500, 450, 150, 10, (150, 150, 150))
box2 = Box(150, 300, 100, 10, (150, 150, 150))
box3 = Box(350, 150, 50, 10, (150, 150, 150))
boxes = (box1, box2, box3)

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Silksong 2')

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))
font = pygame.font.Font(None, 36)
text = font.render("Silksong 2", 1, (200, 200, 200))
textpos = text.get_rect()
textpos.centerx = background.get_rect().centerx
background.blit(text, textpos)

while True:
    ticks = pygame.time.get_ticks()
    # Controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit()
            if event.key == pygame.K_UP and player_grounded:
                player_y_speed = -0.7
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x_speed -= 0.0001
        if player_x_speed > 0:
            player_x_speed -= 0.0005
        player_moving = True
    elif keys[pygame.K_RIGHT]:
        player_x_speed += 0.0001
        if player_x_speed < 0:
            player_x_speed += 0.0005
        player_moving = True
    else:
        player_moving = False

    player_grounded = False
    won = False

    # Bounds check
    if player_x + player_width + player_x_speed > 800:
        player_x_speed = 0
        player_x = 800 - player_width
    elif player_x + player_x_speed < 0:
        player_x_speed = 0
        player_x = 0
    else:
        player_x += player_x_speed
    if player_y + player_height + player_y_speed >= 600:
        player_y_speed = 0
        player_y = 600 - player_height
        player_grounded = True
    if player_y + player_y_speed < 0:
        player_y_speed = 0
        player_y = 0
    else:
        player_y += player_y_speed

    # Collision
    for box in boxes:
        if box.color_timeout <= 0:
            box.color = (150, 150, 150)
        else:
            box.color_timeout -= 1
        if player_x + player_width > box.x and player_x < box.x + box.width:
            # Hit top of the box
            if player_y + player_height <= box.y and player_y + player_height + player_y_speed >= box.y:
                player_y_speed = 0
                player_y = box.y - player_height
                player_grounded = True
                box.color = (0, 250, 0)
                if box == box3:
                    won = True
            # Hit bottom of the box
            elif player_y >= box.y + box.height and player_y + player_y_speed <= box.y + box.height:
                player_y_speed = 0
                player_y = box.y + box.height
                box.color = (250, 250, 0)
                box.color_timeout = 150
        elif player_y + player_height > box.y and player_y < box.y + box.height:
            pass #TODO: Add side collision?

    # Gravity
    if not player_grounded:
        player_y_speed += 0.001
    # Friction
    if player_grounded and not player_moving and player_x_speed > 0:
        player_x_speed -= 0.0005
    elif player_grounded and not player_moving and player_x_speed < 0:
        player_x_speed += 0.0005

    # Graphics
    background.fill((0, 0, 0))
    player_color = (255, 0, 0)
    if won:
        player_color = ((math.sin(ticks/200) + 1) * 100, (math.sin(ticks/200+math.pi) + 1) * 100, (math.cos(ticks/200) + 1) * 100)
    player_box = pygame.draw.rect(background, player_color, pygame.Rect(player_x, player_y, 50, 100))
    for box in boxes:
        pygame.draw.rect(background, box.color, pygame.Rect(box.x, box.y, box.width, box.height))
    # Text overlay
    text2 = font.render(f"Grounded: {player_grounded}", 1, (200, 200, 200))
    background.blit(text2, (0, 540))
    text3 = font.render(f"Y speed: {player_y_speed}", 1, (200, 200, 200))
    background.blit(text3, (0, 570))
    if not won:
        text = font.render(f"Silksong 2", 1, (200, 200, 200))
        background.blit(text, textpos)
    else:
        text = font.render("YOU WIN!!!!!1!11!!!", 1, (200, 200, 0))
        background.blit(text, textpos)

    screen.blit(background, (0, 0))
    pygame.display.flip()
