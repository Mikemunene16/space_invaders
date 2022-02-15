import pygame

#Initialize the pygame
pygame.init()

#Create the display and screen size
screen = pygame.display.set_mode((800,600))

#Title and Icon
pygame.display.set_caption("Space Invaders") 
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon) 



#Player
playerImg = pygame.image.load('battleship.png')
playerX = 370
playerY = 480


def player(x,y):
    screen.blit(playerImg, (x, y))

#GAME LOOP
running = True
while running:

    #RGB of background color
    screen.fill((0, 0, 0))
    playerX += 0.2
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    


    player(playerX, playerY)
    pygame.display.update()



