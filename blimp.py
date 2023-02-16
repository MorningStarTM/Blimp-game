import pygame

WIDTH   = 1500
HEIGHT  = 750

class Blimp(pygame.sprite.Sprite):
    def __init__(self, x, y, health):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./PNG/blimp.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.health_at_begining = health
        self.health_remaining = health
        self.velocity = 0
        self.last_shot = pygame.time.get_ticks()

    
    def update(self):
        #movement speed
        speed = 8
        #cooldown time
        cooldown = 100 #milliseconds

        #gravity
        self.velocity += 0.5
        print(self.velocity)
        if self.velocity > 9:
            self.velocity = 9
        if self.rect.bottom < 738:
            
            self.rect.y += int(self.velocity)

        #mask
        self.mask = pygame.mask.from_surface(self.image)

        #get pressed key
        key = pygame.key.get_pressed()
        #when left arrow pressed
        if key[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= speed
        
    
    def sprite_groups(self):
        blimp_grp = pygame.sprite.Group()
        return blimp_grp
