# Tennis
#
# v-0.0.2
#
# This project is intended for further analysis of the neural network
#
# Author: AndreyKrip

import pygame
from board import Board

def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))

    bd1 = Board(screen, 50)
    bd2 = Board(screen, 730)

    while True:

        backcolor = (10, 34, 140)
        screen.fill(backcolor)
        bd1.board_draw()
        bd2.board_draw()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


def board_draw(screen):  # draw board
    board_color = (200, 100, 30)
    pygame.draw.rect(screen, board_color, (30, 50, 20, 80))


if __name__ == '__main__':
    main()
