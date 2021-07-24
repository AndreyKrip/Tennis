
import pygame

class Ball:

    def __init__(self, screen):
        self.screen = screen

        self.color = "red"
        self.radius = 10


    def ball_draw(self):
        pygame.draw.circle(self.screen, self.color,
                           (400, 300), self.radius)