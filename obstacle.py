import pygame

obs_gap = 150
scale = 4

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./PNG/obstacles.png")
        self.image = pygame.transform.scale(self.image, (600, 600))
        self.rect = self.image.get_rect()
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y]

        if position == -1:
            self.rect.topleft = [x, y]

    def update(self):
        #self.mask = pygame.mask.from_surface(self.image)
        self.rect.x -= 5

        if self.rect.x <= -300:
            self.kill()



    