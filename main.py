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

#load blimp image
blimp = pygame.image.load('./PNG/blimp.png')
blimp_x = 100
blimp_y = 90
blimp_vel = 0.1
blimp_rect = blimp.get_rect()
blimp_rect.center = [blimp_x, blimp_y]

scroll = 0
tiles = math.ceil(WIDTH / bg_width) + 1
gravity = 0.01

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

    #draw glider
    SCREEN.blit(blimp, (blimp_rect.center[0], blimp_rect.center[1]))

    
    """     Adding Physics      """
    #Gravity pulls object 
    if blimp_rect.bottom < 700:
        blimp_rect.y += blimp_vel
        blimp_vel += gravity
        print(blimp_rect.center)
    
    

    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                blimp_rect.y -= 60
    pygame.display.update()
pygame.quit()