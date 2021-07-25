# Tennis
#
# v-0.0.5
#
# This project is intended for further analysis of the neural network
#
# Author: AndreyKrip

import pygame
from board import Board
from ball import Ball


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 600))

    bd1 = Board(screen, 50)
    bd2 = Board(screen, 730)
    ball = Ball(screen)

    while True:


        backcolor = (10, 34, 140)
        screen.fill(backcolor)

        bd1.board_draw()
        bd2.board_draw()

        ball.ball_draw()
        ball.ball_up(bd1, bd2)

        pygame.display.update()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

if __name__ == '__main__':
    main()
