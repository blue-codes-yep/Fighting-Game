# import pygame
# pygame.init()

# win = pygame.display.set_mode((900,567))

# pygame.display.set_caption("Power Rangers ZOMBIES")

# walkRight = [pygame.image.load('images/walk1.png'), pygame.image.load('images/walk2.png'), pygame.image.load('images/walk3.png'), pygame.image.load('images/walk4.png'), pygame.image.load('images/walk5.png'), pygame.image.load('images/walk6.png')]
# walkLeft = [pygame.image.load('images/leftwalk2.png'), pygame.image.load('images/leftwalk3.png'), pygame.image.load('images/leftwalk4.png'), pygame.image.load('images/leftwalk5.png'), pygame.image.load('images/leftwalk6.png'), pygame.image.load('images/leftwalk7.png')]
# bg = pygame.image.load('images/background.png')
# char = pygame.image.load('images/standingstill.png')
# clock = pygame.time.Clock()

# class player(pygame.sprite.Sprite):
#     def __init__(self,x,y,width,height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.vel = 7
#         self.isJump = False
#         self.left = False
#         self.right = False
#         self.walkCount = 0
#         self.jumpCount = 10

#     def draw(self, win):
#         if self.walkCount + 1 >= 18:
#             self.walkCount = 0

#         if self.left:
#             win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
#             self.walkCount += 1
#         elif self.right:
#             win.blit(walkRight[self.walkCount//3], (self.x,self.y))
#             self.walkCount +=1
#         else:
#             win.blit(char, (self.x,self.y))

# def redrawGameWindow():
#     win.blit(bg, (0,0))
#     man.draw(win)
    
#     pygame.display.update()

# #mainloop
# man = player(100, 340, 40, 60)
# run = True
# while run:
#     clock.tick(27)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#     keys = pygame.key.get_pressed()

#     if keys[pygame.K_LEFT] and man.x > man.vel:
#         man.x -= man.vel
#         man.left = True
#         man.right = False
#     elif keys[pygame.K_RIGHT]: #and man.x < 500 - man.width - man.vel:
#         man.x += man.vel
#         man.right = True
#         man.left = False
#     else:
#         man.right = False
#         man.left = False
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
            
#     redrawGameWindow()

# pygame.quit()














# # x = 100
# # y = 340
# # width = 40
# # height = 60
# # vel = 7




# # ###
# # # class Background(pygame.sprite.Sprite):
# # #     def __init__(self, image_file, location):
# # #         pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
# # #         self.image = pygame.image.load('images/background.png')
# # #         self.rect = self.image.get_rect()
# # #         self.rect.left, self.rect.top = location

# # # BackGround = Background('background.png', [0,0])

# # left = False
# # right = False
# # walkCount = 0



# # def redrawGameWindow():
# #     global walkCount
    
# #     win.blit(bg, (0,0))  
# #     if walkCount + 1 >= 18:
# #         walkCount = 0
        
# #     if left:  
# #         win.blit(walkLeft[walkCount//3], (x,y))
# #         # BackGround.rect.left = BackGround.rect.left + 2.0
# #         # #bg.rect.left = bg.rect.left + 2.0
# #         walkCount += 1                          
# #     elif right:
# #         win.blit(walkRight[walkCount//3], (x,y))
# #         # BackGround.rect.right = BackGround.rect.right + 2.0
# #         # #bg.rect.right = bg.rect.right + 2.0
# #         walkCount += 1
        

# #     else:
# #         win.blit(char, (x, y))
# #         walkCount = 0
        
# #     pygame.display.update() 
    


# # #MAIN LOOP



# # run = True
# # while run:
# #     clock.tick(27)

# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             run = False

# #     keys = pygame.key.get_pressed()
    
# #     if keys[pygame.K_LEFT] and x > vel: 
# #         x -= vel
# #         left = True
# #         right = False

# #     elif keys[pygame.K_RIGHT]: # and x < 500 - vel - width:  
# #         x += vel
# #         left = False
# #         right = True
        
# #     else: 
# #         left = False
# #         right = False
# #         walkCount = 0
        
# #     if not(isJump):
# #         if keys[pygame.K_SPACE]:
# #             isJump = True
# #             left = False
# #             right = False
# #             walkCount = 0
# #     else:
# #         if jumpCount >= -10:
# #             y -= (jumpCount * abs(jumpCount)) * 0.5
# #             jumpCount -= 1
# #         else: 
# #             jumpCount = 10
# #             isJump = False

# #     redrawGameWindow() 
    
    
# # pygame.quit()