import pygame
from pygame.locals import *
from Zombie import *
import math
# Intialize the pygame
pygame.init()

# Create the screen 
screen = pygame.display.set_mode((900, 567))


#Title and Icon
pygame.display.set_caption("Fighting Game")

# Add's logo to the window 
# icon = pygame.image.load('')
# pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('images/character.png')
playerX = 100
playerY = 340
playerX_change = 0

def player(x,y):
    screen.blit(playerImg,(x,y))


# Background

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load('images/background.png')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

BackGround = Background('background.png', [0,0])

#  Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # If keystroke is pressed check right, left.
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            #playerX_change = -2.0
            BackGround.rect.left = BackGround.rect.left + 2.5
        if event.key == pygame.K_RIGHT:
            #playerX_change = 2.0
            BackGround.rect.left = BackGround.rect.left - 2.5
    # for zombie in all_zombies:
    #     zombie.move_towards_player(player)
    # if event.type == pygame.KEYUP:
    #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
    #         BackGround.rect.left = 0
    
    screen.blit(BackGround.image, BackGround.rect)
    all_zombies.update()
    playerX += playerX_change
    player(playerX,playerY)
    all_zombies.draw(screen)
    
    pygame.display.flip()

