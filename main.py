# ---------------------------------
# Project: Python Chess
# Authors: Sebastian Hollabaugh & Austin Koehler
#Date: 8-12-2020
# Desc: A basic game of chess made in python
# ----------------------------------

import sys
import pygame

pygame.init()

Width = 800
Height = 800

WHITE = (255, 255, 255)
GRAY = (220, 220, 220)


player_size = 50
player_pos = [Width/2, Height-2*player_size]

screen = pygame.display.set_mode((Width, Height))

game_over = False

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(GRAY)

    i = 0
    j = 0

    for x in range(32):
        pygame.draw.rect(screen, WHITE, (i, j, 100, 100))
        i += 200
        if (i == 800):
            j += 100
            i = 100
        elif (i == 900):
            j += 100
            i = 0

    # if event.type == pygame.KEYDOWN:

    #     x = player_pos[0]
    #     y = player_pos[1]

    #     if event.key == pygame.K_LEFT:
    #         x -= 5
    #     elif event.key == pygame.K_RIGHT:
    #         x += 5
    #     elif event.key == pygame.K_UP:
    #         y -= 5
    #     elif event.key == pygame.K_DOWN:
    #         y += 5
    #     player_pos = [x, y]

    # screen.fill((0, 0, 0))
    # pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

    pygame.display.update()
