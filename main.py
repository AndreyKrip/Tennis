# Tennis
#
# v-0.0.8
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
    x = 260.0
    x2 = 260.0

    while True:

        backcolor = (10, 34, 140)
        screen.fill(backcolor)

        bd1.board_draw(x)
        x = bd1.board_up()
        bd2.board_draw(x2)
        x2 = bd2.board_up()


        ball.ball_draw()

        ball.ball_up(bd1, bd2)

        pygame.display.update()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    bd1.speed = 5
                if event.key == pygame.K_UP:
                    bd1.speed = -5
                if event.key == pygame.K_w:
                    bd2.speed = 5
                if event.key == pygame.K_s:
                    bd2.speed = -5
            elif event.type == pygame.KEYUP:
                bd1.speed = 0
                bd2.speed = 0


if __name__ == '__main__':
    main()
