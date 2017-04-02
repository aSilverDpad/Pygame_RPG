#!/usr/bin/python2.7

import pygame
import sys
from pygame.locals import *
from load_png import load_png
import spritesheet
from sprite_strip_anim import SpriteStripAnim

class Person(pygame.sprite.Sprite): # {{{1
    def __init__(self, name, type): # {{{2
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.type = type
        self.health = 90
        self.armour = 0
        self.temperature = 36
        self.mana = 10
        #TODO: self.inventory = list of items. create item class
        self.x = 0
        self.y = 0

        self.strips = [SpriteStripAnim('images/stewie_sprites_walking_right.png',(0,0,57,70),4,-1,True,10),
                SpriteStripAnim('images/stewie_sprites_walking_left.png',(0,0,57,70),4,-1,True,10),
                SpriteStripAnim('images/stewie_sprites_shooting.png',(0,0,170,80),5,-1,True,10),
                SpriteStripAnim('images/stewie_sprites_dead.png',(0,0,57,70),4,-1,False,10)]
        self.n = 0 # strip number
        #self.rect = (self.x,self.y,70,76)
        self.image = self.strips[self.n].next()
        self.rect = self.image.get_rect()
        self.strips[self.n].iter()

    def walk_animation(self, dir): # {{{2
        if dir == 'LEFT':
            self.n = 1
            self.x -=1
        elif dir == 'RIGHT':
            self.n = 0
            self.x +=1
            if self.x > 600: # scroll from right side to left of 'new screen'
                self.x = -57
                #TODO: Change background to next background
        elif dir == 'UP':
            self.y -=1
        elif dir == 'DOWN':
            self.y +=1
            if (self.y+70) >=350:
                self.y = (350-70) # height - player height
        self.rect = (self.x,self.y,57,70)
        self.image = self.strips[self.n].next()
        print('Player pos: ')
        print('X: ', self.x, ' Y: ', self.y)
        return self.image
    def get_death_animation(self):
        self.n = 3
        self.rect = (self.x,self.y,57,70)
        self.image = self.strips[self.n].next()
        return self.image

