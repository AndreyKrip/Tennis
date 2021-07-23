# Tennis
#
# v-0.0.1
#
# This project is intended for further analysis of the neural network
#
# Author: AndreyKrip

import pygame

def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        backcolor = (10,34,140)
        screen.fill(backcolor)
        pygame.display.update()

def board_draw():
    pass


if __name__ == '__main__':
    main()



