
import pygame

class Ball:

    def __init__(self, screen):
        self.screen = screen
        self.color = "red"
        self.move = 10
        self.radius = 10

        self.x = 400

    def ball_draw(self):
        self.ball = pygame.draw.circle(self.screen, self.color,
                                       (self.x, 300), self.radius)

    def ball_up(self, bd1, bd2):
        if bd1.board.colliderect(self.ball) or bd2.board.colliderect(self.ball):
            self.move = -self.move

        if self.ball.x == 0:  # Условия поражения
            print("Game over!")
            exit()

        if self.ball.x >= 800:  # Условия победы
            print("Game vin!")
            exit()


        self.x += float(self.move)
        self.ball.centerx = self.x
