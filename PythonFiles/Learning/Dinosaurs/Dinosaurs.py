import pygame

pygame.init()

#Consts
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
BACK_COLOUR = (60, 210, 50)

#Images
PlayerImg1 = pygame.image.load("Dino1.png")
PlayerImg2 = pygame.image.load("Dino2.png")

#Window
display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Dinosaurs")

#Methods
def playerMove(x, y):
    display.blit(PlayerImg1, (x, y))

#Main loop
clock = pygame.time.Clock()
play = True
while play:
    #Inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    
    #Graphics
    display.fill(BACK_COLOUR)
    playerMove(DISPLAY_WIDTH/2 - 32, DISPLAY_HEIGHT/2 - 32)
    pygame.display.update()
    
    clock.tick(60)
    
pygame.quit()
quit()