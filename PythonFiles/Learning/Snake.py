import pygame
import time
import random

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SNAKE_THICKNESS = 10

pygame.init()
gameDisplay = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Game')

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
purple = (255, 0, 255)
cyan = (0, 255, 255)

xPos = int(SCREEN_WIDTH/2)
yPos = int(SCREEN_HEIGHT/2)
direction = 'right'
speed = 0.1
length = 5
bodyPositions = [(xPos - 50, yPos), (xPos - 40, yPos), (xPos - 30, yPos), (xPos - 20, yPos), (xPos - 10, yPos)]
font = pygame.font.SysFont(None, 50)

gameExit = False
gameOver = False
foodEaten = True
foodPos = (0, 0)

def msgToScr(msg, colour):
    screen_text = font.render(msg, True, colour)
    gameDisplay.blit(screen_text, [SCREEN_WIDTH / 2 - 75, SCREEN_HEIGHT / 2 - 25])
    pygame.display.update()

while not gameExit and not gameOver:
    if (xPos, yPos) in bodyPositions:
        gameOver = True
    bodyPositions.append((xPos, yPos))
    if foodPos[0] in range(xPos - SNAKE_THICKNESS, xPos + SNAKE_THICKNESS) and foodPos[1] in range(yPos - SNAKE_THICKNESS, yPos + SNAKE_THICKNESS):
        foodEaten = True
        length += 1
    if not foodEaten:
        pass
    elif foodEaten:
        foodPos = (random.randint(0, SCREEN_WIDTH - SNAKE_THICKNESS), random.randint(0, SCREEN_HEIGHT - SNAKE_THICKNESS))
        foodEaten = False
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, blue, [xPos, yPos, SNAKE_THICKNESS, SNAKE_THICKNESS])
    pygame.draw.rect(gameDisplay, green, [foodPos[0], foodPos[1], SNAKE_THICKNESS, SNAKE_THICKNESS])
    for i in range(length):
        pygame.draw.rect(gameDisplay, black, [bodyPositions[i][0], bodyPositions[i][1], SNAKE_THICKNESS, SNAKE_THICKNESS])
    pygame.display.update()
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            gameExit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if direction != 'right':
                    direction = 'left'
            elif event.key == pygame.K_RIGHT:
                if direction != 'left':
                    direction = 'right'
            elif event.key == pygame.K_UP:
                if direction != 'down':
                    direction = 'up'
            elif event.key == pygame.K_DOWN:
                if direction != 'up':
                    direction = 'down'
    if direction == 'up':
        yPos -= SNAKE_THICKNESS
    elif direction == 'down':
        yPos += SNAKE_THICKNESS
    elif direction == 'left':
        xPos -= SNAKE_THICKNESS
    elif direction == 'right':
        xPos += SNAKE_THICKNESS
    if yPos < 0:
        yPos = SCREEN_HEIGHT - SNAKE_THICKNESS
    elif yPos >= SCREEN_HEIGHT:
        yPos = 0
    elif xPos < 0:
        xPos = SCREEN_WIDTH - SNAKE_THICKNESS
    elif xPos >= SCREEN_WIDTH:
        xPos = 0
    if len(bodyPositions) > length:
        del(bodyPositions[0])
    time.sleep(speed)

if gameExit:
    pygame.quit()
    quit()
if gameOver:
    msgToScr('You lose!', red)
    time.sleep(3)
    pygame.quit()
    quit()
