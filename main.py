import pygame
import math
pygame.init()

WIDTH   = 1500
HEIGHT  = 750
FPS = 60

clock = pygame.time.Clock()

#game window
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Glider")

#load backgound image
bg_img = pygame.image.load('./PNG/image.png').convert()
#resize the image
bg_img = pygame.transform.scale(bg_img, (1500,800))
#get the width
bg_width = bg_img.get_width()



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

        
    pygame.display.update()
pygame.quit()