import pygame
import math
from blimp import Blimp
from obstacle import Obstacle

pygame.init()

WIDTH   = 1800
HEIGHT  = 1000
FPS = 60
obs_gap = 150

clock = pygame.time.Clock()

#game window
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Glider")

#load backgound image
bg_img = pygame.image.load('./PNG/image.png').convert()
#resize the image
bg_img = pygame.transform.scale(bg_img, (1500,1000))
#get the width
bg_width = bg_img.get_width()


#blimp
blimp  = Blimp(70, 400, 10)
blimp_group = pygame.sprite.Group()
blimp_group.add(blimp)


#obstacle
obs1 = Obstacle(600, 300, 1)
obs2 = Obstacle(600, 600, -1)
obs_group = pygame.sprite.Group()
obs_group.add(obs1)
obs_group.add(obs2)


scroll = 0
tiles = math.ceil(WIDTH / bg_width) + 1


#window loop
run = True
while run:

    clock.tick(FPS)

    #scrolling background
    for i in range(0, tiles):
        SCREEN.blit(bg_img, (i * bg_width + scroll, 0))
    #scroll background
    scroll -= 5

    if abs(scroll) > bg_width:
        scroll = 0

    


    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    #draw the blimp on screen
    blimp_group.draw(SCREEN)
    #blimp movement
    blimp.update()


    #draw the obstacle
    obs_group.draw(SCREEN)
    #obstacle movement
    obs_group.update()
        
    pygame.display.update()
pygame.quit()