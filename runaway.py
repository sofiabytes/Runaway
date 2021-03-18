import pygame, sys
#import pygame._view
from pygame.locals import *
import functions
import random

pygame.init()

#Setting up window
WINDOWHEIGHT=600
WINDOWWIDTH=800
DISPLAYSURF=pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('You must survive!')

#Naming colours
BLACK=(0, 0, 0)
WHITE=(255, 255, 255)
RED=(255, 0, 0)
GREEN=(0, 255, 0)
BLUE=(0, 0, 255)

#Starting positions and speed for enemy ships
leftx=10
lefty=random.randint(10, 490)
rightx=690
righty=random.randint(10, 490)
leftmove=25
rightmove=25

#importing resources
lasernoise=pygame.mixer.Sound('res/laser1.wav')
rightEnemy=pygame.image.load('res/rightEnemy.png')
leftEnemy=pygame.image.load('res/leftEnemy.png')
player=pygame.image.load('res/player.png')
rightEnemy=pygame.transform.scale(rightEnemy, (100, 100))
leftEnemy=pygame.transform.scale(leftEnemy, (100, 100))
player=pygame.transform.scale(player, (70, 100))

#Number of lives
ll=3
rl=3
pl=3

#Text boxes
fontObj=pygame.font.Font('freesansbold.ttf', 32)
plivestext=fontObj.render('plives: '+str(pl), True, GREEN, BLUE)
textRectObj=plivestext.get_rect()
textRectObj.center=(500, 450)

leftlivestext=fontObj.render(str(ll), True, GREEN, BLUE)
leftrect=leftlivestext.get_rect()
leftrect.center=(200, 150)

rightlivestext=fontObj.render(str(rl), True, GREEN, BLUE)
rightrect=rightlivestext.get_rect()
rightrect.center=(600, 150)

#Define instruction strings
starttext1=fontObj.render('Use up and down to avoid the bullets', True, RED, BLUE)
startrect1=starttext1.get_rect()
startrect1.center=(400, 200)
starttext2=fontObj.render('Wait for the others to shoot each other', True, RED, BLUE)
startrect2=starttext2.get_rect()
startrect2.center=(400, 300)
starttext3=fontObj.render('Press Enter to continue', True, RED, BLUE)
startrect3=starttext3.get_rect()
startrect3.center=(400, 400)

#define laser variables
leftlaserx=0
leftlasery=0
rightlaserx=0
rightlasery=0

while True:
    #Reset settings 
    leftlives=ll
    rightlives=rl
    plives=pl
    #location of player
    kx=350
    ky=250
    
    leftlaser=False
    rightlaser=False

    start=True
    while start:
        #Display instructions
        DISPLAYSURF.fill(BLACK)
        DISPLAYSURF.blit(starttext1, startrect1)
        DISPLAYSURF.blit(starttext2, startrect2)
        DISPLAYSURF.blit(starttext3, startrect3)
        #Get response
        pygame.display.update()        
        for event in pygame.event.get():
            if event.type==QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif (event.type==KEYUP and event.key==K_RETURN):
                start=False

    game=True
    end=True
    pygame.display.update()

    while game:
        #Update box positions
        (lefty, righty, leftmove, rightmove)=functions.box_update(lefty, righty, leftmove, rightmove)
        #Update laser positions
        (leftlaserx, leftlasery, rightlaserx, rightlasery, leftlaser, rightlaser)=functions.laserres(leftlaser, rightlaser, leftlaserx, leftlasery, leftx, lefty, rightlaserx, rightlasery, rightx, righty, lasernoise)
        #Display text
        DISPLAYSURF.fill(BLACK)

        textSurfaceObj=fontObj.render('Player lives: '+str(plives), True, GREEN, BLUE)
        leftlivestext=fontObj.render('Left lives: '+str(leftlives), True, GREEN, BLUE)
        rightlivestext=fontObj.render('Right lives: '+str(rightlives), True, GREEN, BLUE)

        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        DISPLAYSURF.blit(leftlivestext, leftrect)
        DISPLAYSURF.blit(rightlivestext, rightrect)
		
        #Display players
        DISPLAYSURF.blit(leftEnemy, (leftx, lefty))
        DISPLAYSURF.blit(rightEnemy, (rightx, righty))
        DISPLAYSURF.blit(player, (kx, ky))
        pygame.draw.rect(DISPLAYSURF, RED, (leftlaserx, leftlasery, 10, 2))
        pygame.draw.rect(DISPLAYSURF, RED, (rightlaserx, rightlasery, 10, 2))

        #Laser updates
        if (leftlaserx>(kx-10) and leftlaserx<(kx+100) and leftlasery>(ky-2) and leftlasery<(ky+100)):
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)
            leftlaserx=900
            plives-=1
        if (rightlaserx>(kx-10) and rightlaserx<(kx+100) and rightlasery>(ky-2) and rightlasery<(ky+100)):
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)
            rightlaserx=0
            plives-=1

        if (rightlaserx>(leftx-10) and rightlaserx<(leftx+100) and rightlasery>(lefty-2) and rightlasery<(lefty+100)):
            leftlives-=1
            rightlaserx=0
        if (leftlaserx>(rightx-10) and leftlaserx<(rightx+100) and leftlasery>(righty-2) and leftlasery<(righty+100)):
            rightlives-=1
            leftlaserx=900

        pygame.time.wait(100)
        
        #Quit code
        for event in pygame.event.get():
            if event.type==QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type==KEYUP:
                if (event.key==K_UP and ky>10):
                    ky-=10
                elif (event.key==K_DOWN and ky<590):
                    ky+=10
        #Update Display
        pygame.display.update()
    
        (game, deathstr)=functions.dead(plives, rightlives, leftlives) 
    
    while end:
        deathtext=fontObj.render(deathstr, True, GREEN, BLUE)
        deathrects=deathtext.get_rect()
        deathrects.center=(400, 300)   
        DISPLAYSURF.blit(deathtext, deathrects)
        DISPLAYSURF.blit(starttext3, startrect3)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type==KEYUP and event.key==K_RETURN:
                end=False
