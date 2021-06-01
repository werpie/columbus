import pygame
from pygame.math import Vector2


class paprociara():

    def __init__(self, game):
        self.game = game

        self.pozycja = Vector2(0, 0)

    def tick(self):
        # input
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_s]:
            self.pozycja += Vector2(0, 1)
        elif pressed[pygame.K_w]:
            self.pozycja += Vector2(0, -1)
        elif pressed[pygame.K_a]:
            self.pozycja += Vector2(-1, 0)
        elif pressed[pygame.K_d]:
            self.pozycja += Vector2(1, 0)


    def draw(self):
        rect = pygame.Rect(self.pozycja.x, self.pozycja.y, 16, 16)
        pygame.draw.rect(self.game.screen, (0, 150, 255), rect)

    def collision(self):
        pass