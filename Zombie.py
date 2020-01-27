import pygame
import random
import math


class ZombieEnemy(pygame.sprite.Sprite):
# zwalkRight = [pygame.image.load('images/zombiestandright1.png'), pygame.image.load('images/ztep.png'), pygame.image.load('imageszombiestandright1.png'), pygame.image.load('images/zombiestandright1.png')]

# zwalkLeft = [(pygame.image.load('images/zombiestandleft.png'), pygame.image.load('images/ztepleft.png'), pygame.image.load('images/zombiestandleft.png'), pygame.image.load('images/ztep2.png')]
    def __init__(self, x=144, y=440):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/ztepleft.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speedy = random.randrange(1, 4)
    def move_towards_player(self, player):
        # Find direction vector (dx, dy) between enemy and player.
        dx, dy = player.rect.x - self.rect.x, player.rect.y - self.rect.y
        dist = math.hypot (dx, dy)
        dx, dy = dx / dist, dy / dist # Normalize
        # Move along this normalized vector towards the player
        self.rect.x += dx * 5
        self.rect.y += dy * 0

