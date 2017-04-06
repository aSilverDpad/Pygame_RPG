#!/usr/bin/python2.7
#experimental
import random
import pygame

class Item(pygame.sprite.Sprite):
    def __init__(self, name, type, image): # type can be weapon, food, tool, armour, etc
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.type = type
        self.image = image
        self.x = 0
        self.y = 0
class Weapon(Item): #{{{2
    def __init__(self, name, type, image, dmg_range, range, weapon_type):
        Item.__init__(self, name, type, image)
        self.damage_range = dmg_range
        self.range = range

    def Attack(target): # {{{2
        base_damage = random.randint(damage_range[0],damage_range[1])
        damage_done = (base_damage - target.armour)
        target.Take_damage(damage_done)

class Food(Item):
    def __init__(self, name, type, image, value):
        Item.__init__(self, name, type, image)
        self.usage_value = value

class Potion(Item):
    def __init__(self, name, type, image, value):
        Item.__init__(self, name, type, image)
        self.usage_value = value
        #TODO: have better way of identifying potion types etc.
        #TODO: have an 'emptiness' value or different types. small medium etc

class Tool(Item): # bombs, fishing_poles, shovels etc.
    def __init__(self, name, type, image, uses_left):
        Item.__init__(self, name, type, image)
        self.uses_left = uses_left # before the tool is destroyed
        self.valid_actions = 0 # list of actions the tool can do/use on
