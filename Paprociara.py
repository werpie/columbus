import pygame, sys
from pygame.math import Vector2


class paprociara():

    def __init__(self, game):
        pygame.font.init()
        self.game = game
        self.pozycja = Vector2(0, 0)
        self.life = 5
        self.rect = pygame.Rect(self.pozycja.x, self.pozycja.y, 10, 10)

    def tick(self):
        # input
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_s]:
            self.pozycja += Vector2(0, 1)
        if pressed[pygame.K_w]:
            self.pozycja += Vector2(0, -1)
        if pressed[pygame.K_a]:
            self.pozycja += Vector2(-1, 0)
        if pressed[pygame.K_d]:
            self.pozycja += Vector2(1, 0)

        # collisions
        if self.rect.right >= self.game.screen_width:
            self.pozycja -= Vector2(1, 0)

        if self.rect.left <= 0:
            self.pozycja -= Vector2(-1, 0)

        if self.rect.top <= 0:
            self.pozycja -= Vector2(0, -1)

        if self.rect.bottom >= self.game.screen_hight:
            self.pozycja -= Vector2(0, 1)

        if pygame.Rect.colliderect(self.rect, self.game.end):
            sys.exit()

        i = pygame.Rect.collidelist(self.rect, self.game.wall_list)

        if i != -1:
            self.life -= 1
            self.pozycja = Vector2(0, 0)

        if self.life == 0:
            sys.exit()



    def draw(self):
        self.rect = pygame.Rect(self.pozycja.x, self.pozycja.y, 10, 10)
        pygame.draw.rect(self.game.screen, (0, 150, 255), self.rect)
        font = pygame.font.SysFont('Times', 24)
        text1 = font.render('Life:', True, [255, 0, 0])
        text2 = font.render(str(round(self.life)), True, [255, 0, 0])
        self.game.screen.blit(text1, (0, 230))
        self.game.screen.blit(text2, (50, 230))
        pygame.display.flip()



