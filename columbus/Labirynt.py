import pygame
import sys
from Paprociara import paprociara
from pygame.math import Vector2


class Game(object):
    def __init__(self):
        # konfiguracja
        self.speed = 60
        # inicjalizacja
        pygame.init()
        self.screen_width = 462
        self.screen_hight = 256
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_hight))
        self.wall_list = []
        self.pozycja = Vector2(0, 0)
        self.map =  """                             
     wwwwwwwwwwwwwwwwwwwwwwww
                            w
wwwwwwwwwwwwwwwwwwwwwwwwwww w
w                         w w
w wwwwwwwwwwwwwwwwwwwwwww w w  
w w                     w w w
w w wwwwwwwwwwwwwwwwwww w w w
w w w                 w w w w
w w wQ       wwww       w w w
w w wwwwwwwwwwwwwwwwwwwww w w
w w                       w w
w wwwwwwwwwwwwwwwwwwwwwwwww w
w                           w
wwwwwwwwwwwwwwwwwwwwwwwwwwwww""".splitlines()[1:]

        self.tps_clock = pygame.time.Clock()
        self.player = paprociara(self)
        self.end = pygame.Rect(-50,-50,-50,-50)

        while True:
            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    sys.exit(0)


            # ticking
            self.tps_clock.tick(self.speed)
            self.tick()
            #renderowanie
            self.screen.fill((0, 0, 0))
            for y, line in enumerate(self.map):
                for x, c in enumerate(line):
                    if c == "w":
                        self.wall = pygame.Rect(x*16, y*16, 16, 16)
                        self.wall_list.append(self.wall)
                        pygame.draw.rect(self.screen, (255, 255, 255), self.wall)
                    elif c == 'Q':
                        self.end = pygame.Rect(x*16, y*16, 16, 16)
                        pygame.draw.rect(self.screen, (255, 0, 0), self.end)
            self.draw()
            pygame.display.flip()

    def tick(self):
        self.player.tick()

    def draw(self):
        self.player.draw()















