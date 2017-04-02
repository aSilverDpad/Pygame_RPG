#!/usr/bin/python2.7

import pygame
from pygame.locals import *
from person import Person
from load_png import load_png
from spritesheet import spritesheet

def main(): # {{{1
    FPS = 120
    frames = FPS / 12
    paused = False
    delay = 10
    interval = 0

    # Initialise screen {{{2
    pygame.init() # Initialise all imported pygame modules
    screen = pygame.display.set_mode((600,450), RESIZABLE)
    pygame.display.set_caption('Basic Pygame')
    pygame.key.set_repeat(delay,interval)

    # Fill background {{{2
    cave_floor = pygame.image.load('images/cave_bg_600_350.png')
    bottom_hud = pygame.image.load('images/bottom_hud.png')
    # list of rects representing single bars of health from the 'health sprite'
    health_bars_list = [ (4,2,8,36),(12,2,8,36),(20,2,7,36),(27,2,8,36),
            (35,2,8,36),(43,2,8,36),(51,2,7,36),(58,2,7,36),(65,2,8,36),
            (73,2,7,36),(80,2,8,36),(88,2,8,36),(96,2,8,36),(104,2,7,36),
            (110,2,7,36),(118,2,8,36),(126,2,8,36),(134,2,6,36)]
    health_bar = spritesheet('images/health_bar.png')
    #health_bar = spritesheet.images_at(health_bars_list)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.blit(cave_floor, cave_floor.get_rect())

    # Init objects {{{2
    player1 = Person('Player1', 'Wizard')

    clock = pygame.time.Clock()
    n = 0
    pic = player1.walk_animation('RIGHT')

    # Event loop {{{2
    while True:
        #TODO: while not paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    pic = player1.walk_animation('RIGHT')
                if event.key == K_LEFT:
                    pic = player1.walk_animation('LEFT')
                if event.key == K_DOWN:
                    pic = player1.walk_animation('DOWN')
                if event.key == K_UP:
                    pic = player1.walk_animation('UP')
                #DEBUG_CODE:
                if event.key == K_w:
                    if player1.health >= 0 and player1.health < 90:
                        player1.health += 1
                        print(player1.health)
                if event.key == K_s:
                    if player1.health <= 90 and player1.health > 0:
                        player1.health -= 1
                        print(player1.health)

        # blit everything to screen
        screen.blit(background, (0,0))
        screen.blit(bottom_hud, (0,350)) # screen height - hud height

        # {{{3 HEALTH_BAR
        images = health_bar.images_at(health_bars_list)
        i = 0 # images position
        n = 5 # bar counter with regard to health
        c = 0 # counter
        while n <= player1.health:
            screen.blit(images[c], (460+i, 360))
            i += 7.5
            n += 5
            c += 1
        # }}}3

        if player1.health > 0:
            screen.blit(pic, player1.rect)
            pygame.display.flip()
            clock.tick(60)
        else:
            for num in range(4):
                screen.blit(player1.get_death_animation(), player1.rect)
                pygame.display.flip()
                clock.tick(60)

            #death_anim = player1.get_death_animation()
            #death_anim.iter()
            #for num in range(4):
                #player1.image = death_anim.next()
                #screen.blit(player1.image, player1.rect)
                #pygame.display.flip()
                ##clock.tick(60)


if __name__ == '__main__':
    main()

