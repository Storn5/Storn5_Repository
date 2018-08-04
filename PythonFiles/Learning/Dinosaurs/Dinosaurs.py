import pygame

pygame.init()

#Consts
DISPLAY_WIDTH = 960
DISPLAY_HEIGHT = 768
BACK_COLOR = (60, 210, 50)
DINO_WIDTH = 39
DINO_HEIGHT = 27
DINO_SPEED = 2
FRAMES_PER_WALK_ANIMATION = 15

#Images
playerImg1 = pygame.image.load("Dino1.png")
playerImg2 = pygame.image.load("Dino2.png")
rockImg = pygame.image.load("Rock.png")

#Window
display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Dinosaurs")

#Methods
def playerShow(x, y):
    if playerOrient:
        display.blit(playerImg, (x, y))
    else:
        display.blit(pygame.transform.flip(playerImg, True, False), (x, y))
def rocksShow():
    for x in range(0, DISPLAY_WIDTH, 64):
        for y in range(0, DISPLAY_HEIGHT, DISPLAY_HEIGHT - 64):
            display.blit(rockImg, (x, y))
    for y in range(0, DISPLAY_HEIGHT, 64):
        for x in range(0, DISPLAY_WIDTH, DISPLAY_WIDTH - 64):
            display.blit(rockImg, (x, y))

#Vars
playerX = DISPLAY_WIDTH/2 - int(DINO_WIDTH/2)
playerY = DISPLAY_HEIGHT/2 - int(DINO_HEIGHT/2)
playerOrient = True
playerImg = playerImg1
playerWalkCounter = 0

#Main loop
clock = pygame.time.Clock()
play = True
while play:
    #Inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        playerY -= DINO_SPEED
    if keys[pygame.K_s]:
        playerY += DINO_SPEED
    if keys[pygame.K_a]:
        playerX -= DINO_SPEED
        playerOrient = False
    if keys[pygame.K_d]:
        playerX += DINO_SPEED
        playerOrient = True
    #Walk boundaries
    if playerX <= 64:
        playerX = 64
    elif playerX >= DISPLAY_WIDTH - (64 + DINO_WIDTH):
        playerX = DISPLAY_WIDTH - (64 + DINO_WIDTH)
    if playerY <= 64:
        playerY = 64
    elif playerY >= DISPLAY_HEIGHT - (64 + DINO_HEIGHT):
        playerY = DISPLAY_HEIGHT - (64 + DINO_HEIGHT)
    #Walk animation
    playerWalkCounter += 1
    if (keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_d]) and playerWalkCounter >= FRAMES_PER_WALK_ANIMATION:
        if playerImg == playerImg1:
            playerImg = playerImg2
        else:
            playerImg = playerImg1
        playerWalkCounter = 0
    #Graphics
    display.fill(BACK_COLOR)
    rocksShow()
    playerShow(playerX, playerY)
    pygame.display.update()
    
    clock.tick(60)
    
pygame.quit()
quit()