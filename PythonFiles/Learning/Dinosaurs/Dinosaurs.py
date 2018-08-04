import pygame

pygame.init()

#Consts
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
BACK_COLOR = (60, 210, 50)
DINO_SPEED = 2
FRAMES_PER_WALK_ANIMATION = 15

#Images
playerImg1 = pygame.image.load("Dino1.png")
playerImg2 = pygame.image.load("Dino2.png")

#Window
display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Dinosaurs")

#Methods
def playerMove(x, y):
    if playerOrient:
        display.blit(playerImg, (x, y))
    else:
        display.blit(pygame.transform.flip(playerImg, True, False), (x, y))

#Vars
playerX = DISPLAY_WIDTH/2 - 32
playerY = DISPLAY_HEIGHT/2 - 32
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
    playerMove(playerX, playerY)
    pygame.display.update()
    
    clock.tick(60)
    
pygame.quit()
quit()