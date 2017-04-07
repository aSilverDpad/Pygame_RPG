#!/usr/bin/python2.7
#experimental
import pygame
from pygame.locals import *
import item

class Inventory():
    def __init__(self):
        self.item_list = []
    def list_items(self):
        for item in self.item_list:
            print(item.name)
    def display_inv(self):
        pass
    def add(self, item):
        self.item_list.append(item)
    def remove(self, item):
        self.item_list.remove(item)
