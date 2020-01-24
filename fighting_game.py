import pygame
from pygame.locals import *
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
#playerImg = pygame.image.load('images/character.png')
playerX = 100
playerY = 340
# playerX_change = 0



walkRight = [pygame.image.load('images/walk1.png'), pygame.image.load('images/walk2.png'), pygame.image.load('images/walk3.png'), pygame.image.load('images/walk4.png'), pygame.image.load('images/walk5.png'), pygame.image.load('images/walk6.png')]
walkLeft = [pygame.image.load('images/walk1.png'), pygame.image.load('images/walk2.png'), pygame.image.load('images/walk3.png'), pygame.image.load('images/walk4.png'), pygame.image.load('images/walk5.png'), pygame.image.load('images/walk6.png')]
#bg = pygame.image.load('bg.jpg')
char = pygame.image.load('images/standingstill.png')

###
clock = pygame.time.Clock()


def player(x,y):
    global walkCount
    # screen.blit(playerImg,(x,y))
    ### Player - add for walk cycle
    left = False
    right = False
    walkCount = 0
    ###
    if walkCount + 1 >= 27:
        walkCount = 0
    if left: # if facing left
        win.blit(walkLeft[walkCount//10], (x,y)) 
        #interget divide walkCounter by 3 to ensure each image
        #is shown 3 times every animation
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//10], (x,y))
        walkCount += 1
    else:
        screen.blit(char, (x,y))
    pygame.display.update()

# Background

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load('images/background.png')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

BackGround = Background('background.png', [0,0])

#  Game Loop
###
pygame.time.delay(100)


running = True
while running:
    clock.tick(27)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    # If keystroke is pressed check right, left.
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            ###
            left = True
            right = False
            #playerX_change = -2.0
            BackGround.rect.left = BackGround.rect.left + 2.0
        elif event.key == pygame.K_RIGHT:
            #playerX_change = 2.0
            ###
            left = False
            right = True
            BackGround.rect.left = BackGround.rect.left - 2.0
        ###
        else: #if character is not moving, set both left and right to false and reset the animation counter (walkcount)
            left = False
            right = False
            walkCount = 0
    
    
    # if event.type == pygame.KEYUP:
    #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
    #         BackGround.rect.left = 0
    
    #playerX += playerX_change
    player(playerX,playerY)
    screen.blit(BackGround.image, BackGround.rect)
    pygame.display.flip()

