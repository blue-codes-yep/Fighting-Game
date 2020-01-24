import pygame
from pygame.locals import *
import random
import math

class ZombieEnemy(pygame.sprite.Sprite):
    def __init__(self, x=300, y=360):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/zombie.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speedy = random.randrange(1, 8)
    # def move_towards_player(self, player):
    #     # Find direction vector (dx, dy) between enemy and player.
    #     dx, dy = player.rect.x - self.rect.x, player.rect.y - self.rect.y
    #     dist = math.hypot (dx, dy)
    #     dx, dy = dx / dist, dy / dist # Normalize
    #     # Move along this normalized vector towards the player
    #     self.rect.x += dx * self.speed
    #     self.rect.y += dy * self.speed


all_zombies = pygame.sprite.Group()


for i in range( 50 ):
    new_x = random.randrange( 0, 10000)       # random x-position
    # new_y = random.randrange( 0, )      # random y-position
    all_zombies.add(ZombieEnemy(new_x))         # create, and add to group

