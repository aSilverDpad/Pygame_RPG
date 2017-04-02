#!/usr/bin/python2.7

import os
import pygame

def load_png(name): # {{{1
    '''Load image and return image object.
        looks for image in ./data
        Returns: image, image rect.'''
    fullname = os.path.join('images', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None: # Transparency
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    return image, image.get_rect()

