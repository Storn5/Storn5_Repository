import pygame
import time

pygame.init()

#Consts
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
PLATFORM_WIDTH = 16
PLATFORM_HEIGHT = 128
BALL_DIAMETER = 32
BALL_SPEED = 10
PLAYER_SPEED = 15
OPPONENT_SPEED = 8
PLAYER_RIGHT_BOUNDARY = DISPLAY_WIDTH / 4

#Import images
playerImg = pygame.image.load('Platform_Blue.png')
opponentImg = pygame.image.load('Platform_Red.png')
ballImg = pygame.image.load('Ball.png')

#Creating window
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('First PyGame game')
clock = pygame.time.Clock()

#Methods
def drawPlayer(x, y):
    gameDisplay.blit(playerImg, (x, y))
def drawOpponent(x, y):
    gameDisplay.blit(opponentImg, (x, y))
def drawBall(x, y):
    gameDisplay.blit(ballImg, (x, y))
def text_objects(text, font):
    textSurface = font.render(text, True, (255, 255, 255))
    return textSurface, textSurface.get_rect()
def drawScore(playerScore, opponentScore):
    scoreText = pygame.font.Font('freesansbold.ttf', 30)
    TextSurf, TextRect = text_objects(str(playerScore) + ' | ' + str(opponentScore), scoreText)
    TextRect.center = (DISPLAY_WIDTH / 2, 30)
    gameDisplay.blit(TextSurf, TextRect)
def drawGoal(who):
    goalText = pygame.font.Font('freesansbold.ttf', 30)
    TextSurf, TextRect = text_objects(who + ' scores!', goalText)
    TextRect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2)
    gameDisplay.blit(TextSurf, TextRect)
def drawTime(t):
    timeText = pygame.font.Font('freesansbold.ttf', 30)
    TextSurf, TextRect = text_objects('Time: ' + str(t), timeText)
    TextRect.center = (80, 30)
    gameDisplay.blit(TextSurf, TextRect)

#Initializing vars
playerX = PLATFORM_WIDTH / 2
playerY = DISPLAY_HEIGHT / 2
playerMoveX = 0
playerMoveY = 0
opponentX = DISPLAY_WIDTH - (PLATFORM_WIDTH / 2)
opponentY = DISPLAY_HEIGHT / 2
opponentMoveX = 0
opponentMoveY = 0
ballX = DISPLAY_WIDTH / 2
ballY = DISPLAY_HEIGHT / 2
ballMoveX = BALL_SPEED
ballMoveY = -BALL_SPEED
playerPoints = 0
opponentPoints = 0

#Main game loop
over = False
while not over:
    
    #Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerMoveX = -PLAYER_SPEED
            elif event.key == pygame.K_RIGHT:
                playerMoveX = PLAYER_SPEED
            if event.key == pygame.K_UP:
                playerMoveY = -PLAYER_SPEED
            elif event.key == pygame.K_DOWN:
                playerMoveY = PLAYER_SPEED
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                playerMoveX = 0
            elif event.key == pygame.K_RIGHT:
                playerMoveX = 0
            if event.key == pygame.K_UP:
                playerMoveY = 0
            elif event.key == pygame.K_DOWN:
                playerMoveY = 0
    
    #Calculate opponent movement
    if ballY > opponentY:
        opponentMoveY = OPPONENT_SPEED
    elif ballY < opponentY:
        opponentMoveY = -OPPONENT_SPEED
    elif ballY == opponentY:
        opponentMoveY = 0
    
    #Calculate positions
    playerX += playerMoveX
    playerY += playerMoveY
    opponentX += opponentMoveX
    opponentY += opponentMoveY
    ballX += ballMoveX
    ballY += ballMoveY
    
    #Check if in boundaries
    #Player
    if playerX < PLATFORM_WIDTH / 2:
        playerX = PLATFORM_WIDTH / 2
    elif playerX > PLAYER_RIGHT_BOUNDARY - (PLATFORM_WIDTH / 2):
        playerX = PLAYER_RIGHT_BOUNDARY - (PLATFORM_WIDTH / 2)
    if playerY < PLATFORM_HEIGHT / 2:
        playerY = PLATFORM_HEIGHT / 2
    elif playerY > DISPLAY_HEIGHT - (PLATFORM_HEIGHT / 2):
        playerY = DISPLAY_HEIGHT - (PLATFORM_HEIGHT / 2)
    #Ball
    if ballX <= BALL_DIAMETER / 2:
        ballX = DISPLAY_WIDTH / 2
        ballY = DISPLAY_HEIGHT / 2
        ballMoveX = BALL_SPEED
        ballMoveY = -BALL_SPEED
        opponentPoints += 1
        drawGoal('Opponent')
        pygame.display.update()
        time.sleep(2)
    elif ballX >= DISPLAY_WIDTH - (BALL_DIAMETER / 2):
        ballX = DISPLAY_WIDTH / 2
        ballY = DISPLAY_HEIGHT / 2
        ballMoveX = BALL_SPEED
        ballMoveY = -BALL_SPEED
        playerPoints += 1
        drawGoal('Player')
        pygame.display.update()
        time.sleep(2)
    if ballY <= BALL_DIAMETER / 2:
        ballY = BALL_DIAMETER / 2
        ballMoveY = -ballMoveY
    elif ballY >= DISPLAY_HEIGHT - (BALL_DIAMETER / 2):
        ballY = DISPLAY_HEIGHT - (BALL_DIAMETER / 2)
        ballMoveY = -ballMoveY
    if ballX <= playerX + (PLATFORM_WIDTH / 2) + (BALL_DIAMETER / 2) and ballX >= playerX - (PLATFORM_WIDTH / 2) + (BALL_DIAMETER / 2) and ballY >= playerY - (PLATFORM_HEIGHT / 2) - (BALL_DIAMETER / 2) and ballY <= playerY + (PLATFORM_HEIGHT / 2) + (BALL_DIAMETER / 2):
        ballX = playerX + (PLATFORM_WIDTH / 2) + (BALL_DIAMETER / 2)
        ballMoveX = -ballMoveX
    elif ballX >= opponentX - (PLATFORM_WIDTH / 2) - (BALL_DIAMETER / 2) and ballX <= opponentX + (PLATFORM_WIDTH / 2) - (BALL_DIAMETER / 2) and ballY >= opponentY - (PLATFORM_HEIGHT / 2) - (BALL_DIAMETER / 2) and ballY <= opponentY + (PLATFORM_HEIGHT / 2) + (BALL_DIAMETER / 2):
        ballX = opponentX - (PLATFORM_WIDTH / 2) - (BALL_DIAMETER / 2)
        ballMoveX = -ballMoveX
    
    #Draw on display
    gameDisplay.fill((0, 0, 0))
    drawPlayer(playerX - (PLATFORM_WIDTH / 2), playerY - (PLATFORM_HEIGHT / 2))
    drawOpponent(opponentX - (PLATFORM_WIDTH / 2), opponentY - (PLATFORM_HEIGHT / 2))
    drawBall(ballX - (BALL_DIAMETER / 2), ballY - (BALL_DIAMETER / 2))
    drawScore(playerPoints, opponentPoints)
    drawTime(int(pygame.time.get_ticks() / 1000))
    
    #Update frame
    pygame.display.update()
    clock.tick(60)

#End
pygame.quit()
quit()
