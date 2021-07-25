

import pygame

class Board:
    def __init__(self, screen, x_pos):

        self.color = (23, 170, 150)
        self.width = 20
        self.height = 80
        self.sc = screen
        self.x_position = x_pos
        self.y_position = (600/2)-self.height/2

    def board_draw(self):

        self.board = pygame.draw.rect(self.sc, self.color, (self.x_position,
                                               self.y_position,
                                               self.width,
                                               self.height))
