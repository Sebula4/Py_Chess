#---------------------------------
#Project: Python Chess
#Authors: Sebastian Hollabaugh & Austin Koehler
#Date: 8-12-2020
#Desc: A basic game of chess made in python
#----------------------------------

import pygame
import sys

pygame.init()

Width = 800
Height = 600

RED = (255,0,0)
player_pos = [400, 300]
player_size = 50

screen = pygame.display.set_mode((Width, Height))

game_over = False

while not game_over:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

    pygame.display.update()

    #print(pygame.get_init())

