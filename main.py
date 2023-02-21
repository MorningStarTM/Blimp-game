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

#frequency of obstacle
obs_frequency = 3000
#last time of obstacle
last_time = pygame.time.get_ticks() - obs_frequency

#game window
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Glider")

#load backgound image
bg_img = pygame.image.load('./PNG/image.png').convert()
#resize the image
bg_img = pygame.transform.scale(bg_img, (1500,1000))
#get the width
bg_width = bg_img.get_width()


all_sprite = pygame.sprite.Group()

#blimp
blimp  = Blimp(70, 400, 10)
blimp_group = pygame.sprite.Group()
blimp_group.add(blimp)

obs_group = pygame.sprite.Group()
#generate the obstacles up & down
def generate_obstacle():
    obs1 = Obstacle(WIDTH, 300, 1)
    #obs2 = Obstacle(WIDTH, 600, -1)
    obs_group.add(obs1)
    all_sprite.add(obs1)
    #obs_group.add(obs2)


bg_scroll = 0
scroll = 5
tiles = math.ceil(WIDTH / bg_width) + 1


#window loop
run = True
while run:

    clock.tick(FPS)
    time_now = pygame.time.get_ticks()

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

    #detect the collision
    if pygame.sprite.spritecollide(blimp, obs_group, False, pygame.sprite.collide_mask):
        run = False



    #draw the blimp on screen
    blimp_group.draw(SCREEN)
    #blimp movement
    blimp.update()


    #draw the obstacle
    obs_group.draw(SCREEN)
    #obstacle movement
    obs_group.update()


    if time_now - last_time > obs_frequency:
        generate_obstacle()
        last_time = time_now
    

    pygame.display.update()
pygame.quit()