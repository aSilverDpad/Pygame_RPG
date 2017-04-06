#!/usr/bin/python2.7

import pygame
from pygame.locals import *
import item

class Inventory(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)
        self.item_list = self.sprites()
    def list_items(self):
        self.item_list = self.sprites()
        for item in self.item_list:
            print(item.name)
    def draw_items(self):
        x,y = 0
        for item in self.item_list:

