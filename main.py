import pygame

#Initialize the pygame
pygame.init()

#Create the display and screen size
screen = pygame.display.set_mode((800,600))

#Title and Icon
pygame.display.set_caption("Space Invaders") 
# icon = pygame.image.load('../static/images/ufo.png')
# pygame.display.set_icon(icon) 

#GAME LOOP
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


