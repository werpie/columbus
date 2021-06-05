import pygame
import sys
from Paprociara import paprociara


class Game(object):
    def __init__(self):
        # konfiguracja
        self.tps_max = 100.0
        # inicjalizacja
        pygame.init()
        self.screen = pygame.display.set_mode((462, 256))
        self.tile = pygame.image.load("square.png")
        self.end = pygame.image.load("end.png")
        self.map =  """                             
wwwww  www   www  ww   ww  ww
w             w             w
w                           w
w    wwwwww    wwwww      www
www    w                  w w
w      w          w         w
w   wwwww     wwwwwww      ww
w      wwwwww     w     w   w
w    w      w   Qwww  wwww   w
w      w          w     w   w
w   wwwwww www wwww     w   w
w     w              ww w   w
w                           w
wwwwwwwwwwwwwwwwwwwwwwwwwwwww""".splitlines()[1:]

        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0
        self.player = paprociara(self)

        while True:
            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    sys.exit(0)
                # elif self.player.pozycja == self.end.pozycja:
                    sys.exit(0)

            # ticking
            self.tps_delta += self.tps_clock.tick() / 1000.0  # czas wykonania klatki
            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -= 1 / self.tps_max

            #renderowanie
            self.screen.fill((0, 0, 0))
            for y, line in enumerate(self.map):
                for x, c in enumerate(line):
                    if c == "w":
                        self.screen.blit(self.tile, (x * 16, y * 16))
                    elif c == 'Q':
                        self.screen.blit(self.end, (x * 16, y * 16))
            self.draw()
            pygame.display.flip()

    def tick(self):
        self.player.tick()

    def draw(self):
        self.player.draw()


if __name__ == '__main__':
    Game()













