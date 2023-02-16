import pygame


class Blimp(pygame.sprite.Sprite):
    def __init__(self, x, y, health):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./PNG/blimp.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.health_at_begining = health
        self.health_remaining = health
        self.last_shot = pygame.time.get_ticks()

    
    def update(self):
        pass
