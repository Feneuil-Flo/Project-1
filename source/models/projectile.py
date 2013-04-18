# -*-coding:Latin-1 -*

import pygame
from pygame.locals import *
import math

from random import randrange
from helper.loaders import load_image
from constants import NB_SQUARES_PER_ROW, NB_SQUARES_PER_COL, SQUARE_SIDE
import globals

class Projectile(pygame.sprite.Sprite):
    """Classe meres des projectiles"""
    def __init__(self,x0,y0,angle0):

        pygame.sprite.Sprite.__init__(self)
        self.vit=0
        self.rect = pygame.Rect(x0,y0,8,8)
        self.aim = angle0  # un angle en radian
    
    def update(self):
        self.cpt-=1
        if self.cpt==0:
            self.kill()
            return
        
        
        
        
        #test de collision
        ghost = pygame.sprite.Sprite()
        
        deltaX = self.vit*math.cos(self.aim)
        ghost.rect = pygame.Rect(self.rect.left+deltaX,self.rect.top,8,8)
        if len(pygame.sprite.spritecollide(ghost, globals.obstacle, False))!=0:
            self.aim = (3.1416 - self.aim)
        
        deltaY = -self.vit*math.sin(self.aim)
        ghost.rect = pygame.Rect(self.rect.left,self.rect.top+deltaY,8,8)
        if len(pygame.sprite.spritecollide(ghost, globals.obstacle, False))!=0:
            self.aim = -self.aim
            

        
        x=(self.rect.left+self.vit*math.cos(self.aim))%(NB_SQUARES_PER_ROW*SQUARE_SIDE)
        y=(self.rect.top-self.vit*math.sin(self.aim))%(NB_SQUARES_PER_COL*SQUARE_SIDE)
        
        self.rect=pygame.Rect(x,y,8,8)
        self.switchSprite()
        
    def switchSprite(self):
        if False:
            print('PWeT PwEET')
        
    

class Balle(Projectile):
    def __init__(self,x0,y0, angle0):
        
        Projectile.__init__(self,x0,y0,angle0)
        self.vit=10
        self.cpt=1000
        #self.im1 = load_image('reddragon1.png')[0].convert()
        #self.im2 = load_image('reddragon2.png')[0].convert()
        #self.im3 = load_image('reddragon3.png')[0].convert()
        #self.im4 = load_image('reddragon4.png')[0].convert()
        #self.image=self.im1
        self.im1 = load_image('Balle.png')[0].convert()
        self.im2 = load_image('Balle.png')[0].convert()
        self.im3 = load_image('Balle.png')[0].convert()
        self.im4 = load_image('Balle.png')[0].convert()
        self.image=self.im1
        self.image.set_colorkey((255,255,255))
        
    def switchSprite(self):
        t=self.cpt%20
        if t>14:
            self.image=self.im1
        elif t>9:
            self.image=self.im2
        elif t>4:
            self.image=self.im3
        else:
            self.image=self.im4
        self.image.set_colorkey((255,255,255))
