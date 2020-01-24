import pygame
import math
import random
from Zombie import *
# from pygame.locals import *
pygame.init()

win = pygame.display.set_mode((900,567))

pygame.display.set_caption("Power Rangers ZOMBIES")

walkRight = [pygame.image.load('images/walk1.png'), pygame.image.load('images/walk2.png'), pygame.image.load('images/walk3.png'), pygame.image.load('images/walk4.png'), pygame.image.load('images/walk5.png'), pygame.image.load('images/walk6.png')]
walkLeft = [pygame.image.load('images/leftwalk2.png'), pygame.image.load('images/leftwalk3.png'), pygame.image.load('images/leftwalk4.png'), pygame.image.load('images/leftwalk5.png'), pygame.image.load('images/leftwalk6.png'), pygame.image.load('images/leftwalk7.png')]
bg = pygame.image.load('images/background.png')
char = pygame.image.load('images/standingstill.png')
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        self.image = pygame.Surface((144,200))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 0
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.rect.x = x
        self.rect.y = y
        # ###
        # self.hitbox = (#draw a rectangle that acts as hitbox)
        # ###
    def draw(self, win):
        if self.walkCount + 1 >= 18:
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1
        else:
            win.blit(char, (self.x,self.y))

# #################
#     def attack(self, hitbox):
#         self.hitbox
#         if self.left == True:
#             #draw a hitbox going left
#             #animation for hitting left
#             #check for hitbox collision
#             # if collision do the thing
#             # end attack animation/ go back to normal animation
#             # destroy attack hitbox
#         elif self.right == True:
#             #draw a hitbox going right
#             #animation for hitting right
#             #check for hitbox collision
#             #if collision do the thing 
#             # end attack animation/ go back to normal animation
#             #destroy attack hitbox

        ################

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load('images/background.png')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

BackGround = Background('images/background.png', [0,0])

# def redrawGameWindow():
#     win.blit(bg, (0,0))
#     man.draw(win)
    
#     pygame.display.update()
all_zombies = pygame.sprite.Group()





#mainloop
man = Player(100, 340, 40, 60)
run = True
for i in range( 50 ):
    new_x = random.randrange( 0, 10000)       # random x-position
    # new_y = random.randrange( 0, )      # random y-position
    z = ZombieEnemy(new_x)
    all_zombies.add(z)         # create, and add to group
    z.move_towards_player(man)

    #####
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
# #################
#     if keys[pygame.K_LCTRL]:
#         attack() # add hitbox

# #################
    if keys[pygame.K_LEFT] and man.x > man.vel:
        BackGround.rect.left = BackGround.rect.left + int(10)
        man.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT]: #and man.x < 500 - man.width - man.vel:
        BackGround.rect.left = BackGround.rect.left - int(10)
        man.x += man.vel
        man.right = True
        man.left = False
    else:
        man.right = False
        man.left = False
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
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
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
    pygame.display.flip()
    

pygame.quit()










# import pygame
# import math
# import random
# from Zombie import *
# # from pygame.locals import *
# pygame.init()

# win = pygame.display.set_mode((900,567))

# pygame.display.set_caption("Power Rangers ZOMBIES")

# walkRight = [pygame.image.load('images/walk1.png'), pygame.image.load('images/walk2.png'), pygame.image.load('images/walk3.png'), pygame.image.load('images/walk4.png'), pygame.image.load('images/walk5.png'), pygame.image.load('images/walk6.png')]
# walkLeft = [pygame.image.load('images/leftwalk2.png'), pygame.image.load('images/leftwalk3.png'), pygame.image.load('images/leftwalk4.png'), pygame.image.load('images/leftwalk5.png'), pygame.image.load('images/leftwalk6.png'), pygame.image.load('images/leftwalk7.png')]
# bg = pygame.image.load('images/background.png')
# char = pygame.image.load('images/standingstill.png')
# clock = pygame.time.Clock()

# class Player(pygame.sprite.Sprite):
#     def __init__(self,x,y,width,height):
#         self.image = pygame.Surface((144,200))
#         self.rect = self.image.get_rect()
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.vel = 0
#         self.isJump = False
#         self.left = False
#         self.right = False
#         self.walkCount = 0
#         self.jumpCount = 10
#         self.rect.x = x
#         self.rect.y = y
#         self.standing = True

#     def draw(self, win):
#         if self.walkCount + 1 >= 18:
#             self.walkCount = 0


#     ##  
#         if not(self.standing):
#             if self.left:
#                 win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
#                 self.walkCount += 1
#             elif self.right:
#                 win.blit(walkRight[self.walkCount//3], (self.x,self.y))
#                 self.walkCount +=1
#         else:
#             if self.right:
#                 win.blit(walkRight[0], (self.x, self,y))
#             else:
#                 win.blit(walkLeft[0], (self.x, self.y))




# # PROJECTILE CLASS ---- sword
# class projectile(object):
#     def __init__(self,x,y,radius,color,facing):
#         self.x = x
#         self.y = y
#         self.radius = radius
#         self.color = color
#         self.facing = facing
#         self.vel = 8 * facing

#     def draw(self,win):
#         pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

# class Background(pygame.sprite.Sprite):
#     def __init__(self, image_file, location):
#         pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
#         self.image = pygame.image.load('images/background.png')
#         self.rect = self.image.get_rect()
#         self.rect.left, self.rect.top = location

# BackGround = Background('images/background.png', [0,0])

# # def redrawGameWindow():
# #     win.blit(bg, (0,0))
# #     man.draw(win)
    
# #     pygame.display.update()
# all_zombies = pygame.sprite.Group()



# facing = 0
# bullets = []
# #mainloop
# man = Player(100, 340, 40, 60)
# run = True
# for i in range( 50 ):
#     new_x = random.randrange( 0, 10000)       # random x-position
#     # new_y = random.randrange( 0, )      # random y-position
#     z = ZombieEnemy(new_x)
#     all_zombies.add(z)         # create, and add to group
#     z.move_towards_player(man)

#     #####






# while run:
#     clock.tick(27)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#     keys = pygame.key.get_pressed()
#     #bullet shit
#     if keys[pygame.K_LCTRL]:
#         if man.left:
#             facing = -1
#         else:
#             facing = 1

#     if len(bullets) < 5:
#         bullets.append(projectile(round(man.x+man.width//2), round(man.y + man.height//2), 6, (0,0,0), facing))

#     if keys[pygame.K_LEFT] and man.x > man.vel:
#         BackGround.rect.left = BackGround.rect.left + int(10)
#         man.x -= man.vel
#         man.left = True
#         man.right = False
#         man.standing = False
#     elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
#         BackGround.rect.left = BackGround.rect.left - int(10)
#         man.x += man.vel
#         man.right = True
#         man.left = False
#         man.standing = False
#     else:
#         man.standing = True
#         man.walkCount = 0
        
#     if not(man.isJump):
#         if keys[pygame.K_SPACE]:
#             man.isJump = True
#             man.right = False
#             man.left = False
#             man.walkCount = 0
#     else:
#         if man.jumpCount >= -10:
#             neg = 1
#             if man.jumpCount < 0:
#                 neg = -1
#             man.y -= (man.jumpCount ** 2) * 0.5 * neg
#             man.jumpCount -= 1
#         else:
#             man.isJump = False
#             man.jumpCount = 10
            
#     # redrawGameWindow()
#     for zombie in all_zombies:
#         zombie.move_towards_player(man)
#     #BULLETS
#     for bullet in bullets:
#         if bullet.x < 500 and bullet.x > 0:
#             bullet.x += bullet.vel  
#         else:
#             bullets.pop(bullets.index(bullet))

#     win.blit(BackGround.image, BackGround.rect)
#     all_zombies.update()
#     man.draw(win)
#     #bullets
#     for bullet in bullets:
#         bullet.draw(win)
    
#     pygame.display.update()
#     all_zombies.draw(win)
#     pygame.display.flip()
    

# pygame.quit()