
import pygame

class Ball:

    def __init__(self, screen):
        self.screen = screen
        self.color = "red"
        self.move_x = 2
        self.move_y = 2
        self.radius = 10

        self.x = 400
        self.y = 300

    def ball_draw(self):
        self.ball = pygame.draw.circle(self.screen, self.color,
                                       (self.x, self.y), self.radius)

    def ball_up(self, bd1, bd2):
        if bd1.board.colliderect(self.ball) or bd2.board.colliderect(self.ball):
            self.move_x = -self.move_x

        if self.ball.x == 0:  # Условия поражения
            print("Game over!")
            exit()

        if self.ball.x >= 800:  # Условия победы
            print("Game vin!")
            exit()

        if self.ball.y >= 600 or not self.ball.y:
            self.move_y *= -1



        self.x += float(self.move_x)
        self.ball.centerx = self.x


        self.y += float(self.move_y)
        self.ball.centery = self.y