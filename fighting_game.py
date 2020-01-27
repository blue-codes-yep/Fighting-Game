import pygame
import math
import random
from Zombie import *

pygame.init()

win = pygame.display.set_mode((900,567))
pygame.display.set_caption("Power Rangers ZOMBIES")
WHITE = (255,255,255)

#add music
song = 'theme2.ogg'
pygame.mixer.music.load(song)

walkRight = [pygame.image.load('images/walk1.png'), pygame.image.load('images/walk2.png'), pygame.image.load('images/walk3.png'), pygame.image.load('images/walk4.png'), pygame.image.load('images/walk5.png'), pygame.image.load('images/walk6.png')]
walkLeft = [pygame.image.load('images/leftwalk2.png'), pygame.image.load('images/leftwalk3.png'), pygame.image.load('images/leftwalk4.png'), pygame.image.load('images/leftwalk5.png'), pygame.image.load('images/leftwalk6.png'), pygame.image.load('images/leftwalk7.png')]
bg = pygame.image.load('images/background.png')
attackTime = [pygame.image.load('images/sliceplaceholder.png')]
char = pygame.image.load('images/standingstill.png')
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        self.image = pygame.Surface((144,200))
        self.rect = self.image.get_rect()
        self.width = width
        self.height = height
        self.vel = 0
        self.isJump = False
        self.left = False
        self.right = False
        self.attack = False
        self.walkCount = 0
        self.jumpCount = 10
        self.rect.x = x
        self.rect.y = y

    def draw(self, win):
        if self.walkCount + 1 >= 18:
            self.walkCount = 0
        if self.left:
            win.blit(walkLeft[self.walkCount//3], (self.rect.x,self.rect.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount//3], (self.rect.x,self.rect.y))
            self.walkCount +=1
        elif self.attack:
            win.blit(attackTime[self.walkCount//3], (self.rect.x,self.rect.y))
        else:
            win.blit(char, (self.rect.x,self.rect.y))

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load('images/background.png')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

### added for titlescreen
class Titlescreen(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/titlescreen1.png')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

### added for titlescreen
TitleScreen = Titlescreen('images/titlescreen1.png', [0,0])
BackGround = Background('images/background.png', [0,0])
### added for titlescreen
def game_intro():

    intro = True

    while intro == True:
        for event in pygame.event.get():
            print(event)
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        win.blit(TitleScreen.image, TitleScreen.rect)
        pygame.display.update()
        intro = False
        clock.tick(0.5)

BackGround = Background('images/background.png', [0,0])

all_zombies = pygame.sprite.Group()

#

#mainloop
man = Player(100, 340, 40, 60)
run = True

for i in range( 50 ):
    new_x = random.randrange( 0, 10000)       # random x-position
    z = ZombieEnemy(new_x)
    all_zombies.add(z)         # create, and add to group
    z.move_towards_player(man)

    #####
textbesidescore = 'Score: '
score = 0

#music time
pygame.mixer.music.play(-1)
### added for titlescreen
while game_intro():
        if keys[pygame.K_SEMICOLON]:
            intro = False
            break
        else:
            game_intro()

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    ## Collide
    if pygame.sprite.spritecollide(man, all_zombies, dokill=True):
       score += 1
       print(score)

        

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.rect.x > man.vel:
        BackGround.rect.left = BackGround.rect.left + int(10)
        man.rect.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT]: #and man.x < 500 - man.width - man.vel:
        BackGround.rect.left = BackGround.rect.left - int(10)
        man.rect.x += man.vel
        man.right = True
        man.left = False
        #### attack
    elif keys[pygame.K_UP]: 
        man.right = False
        man.left = False
        man.attack = True
        man.walkCount = 0
    else:
        man.right = False
        man.left = False
        man.attack = False
        man.walkCount = 0
        
    if not(man.isJump):
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.rect.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
            
    # redrawGameWindow()
    for zombie in all_zombies:
        zombie.move_towards_player(man)
    
    win.blit(BackGround.image, BackGround.rect)
    all_zombies.update()
    man.draw(win)
    all_zombies.draw(win)
    
    font = pygame.font.Font(None, 74)
    text = font.render(str(score), 1, WHITE)
    text2 = font.render(textbesidescore, 1, WHITE)
    win.blit(text, (490, 14))
    win.blit(text2, (330,11))
    pygame.display.flip()
    

pygame.quit()