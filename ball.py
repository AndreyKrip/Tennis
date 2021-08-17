
import pygame

class Ball:

    def __init__(self, screen):
        self.screen = screen
        self.color = "red"
        self.move_x = 4
        self.move_y = 0
        self.radius = 10

        self.x = 400
        self.y = 300

    def ball_draw(self):
        self.ball = pygame.draw.circle(self.screen, self.color,
                                       (self.x, self.y), self.radius)

    def ball_up(self, bd1, bd2, screen_rect):
        if not self.ball.colliderect(screen_rect):
            self.move_y *= -1
        
    
        if bd1.board.colliderect(self.ball) or bd2.board.colliderect(self.ball):
            if bd1.speed > 0 or bd2.speed > 0:
                self.move_y += 1
            elif bd1.speed < 0 or bd2.speed < 0:
                self.move_y -= 1

            self.move_x = -self.move_x

        if self.ball.x == 0:  # Условия поражения
            print("Game over!")
            exit()

        if self.ball.x >= 800:  # Условия победы
            print("Game vin!")
            exit()

        self.x += float(self.move_x)
        self.ball.centerx = self.x

        self.y += float(self.move_y)
        self.ball.centery = self.y