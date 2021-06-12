import pygame
from pygame.math import Vector2
BLACK = (0,0,0)
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
SCREEN_SIZE = (800,800)

"""
Wywołujemy funkcję za pomocą planet_choosing()
Jeżeli nie podamy do środka niczego, to pokaże tylko 2 planety,
Jeżeli podamy do niego True, to pokaże się trzecia planeta, którą będzie można wybrać
Funkcja zwraca wartości 1 i 2 dla planet widoczych normalnie i 3 dla księżyca
"""

def init_display():
    global screen,background,font
    screen = pygame.display.set_mode((SCREEN_SIZE))
    background = pygame.Surface(screen.get_size())
    background = pygame.image.load("photos/tlo.jpg")
    font = pygame.font.SysFont("Times",20)

class crosshair():

    def __init__(self):
        self.white()
        self.position = Vector2(SCREEN_HEIGHT/2, SCREEN_WIDTH/2)

    def move(self,dir):

        distance = 7
        if dir == "N":
            self.position -= Vector2(0,distance)
        if dir == "E":
            self.position += Vector2(distance,0)
        if dir == "S":
            self.position += Vector2(0,distance)
        if dir == "W":
            self.position -= Vector2(distance,0)
        self.even()

    def even(self):
        if self.position[0] < 10:
            self.position = (10,self.position[1])
        if self.position[0] > SCREEN_WIDTH-10:
            self.position = (990,self.position[1])
        if self.position[1] < 10:
            self.position = (self.position[0],10)
        if self.position[1] > SCREEN_HEIGHT:
            self.position = (self.position[0],SCREEN_HEIGHT-10)

    def position_raw(self):
        return (self.position[0]-1733,self.position[1]-961)

    def position_on_map(self):
        return self.position

    def green(self):
        global aim_image
        aim_image = pygame.image.load("photos/celownik_active.png")

    def white(self):
        global aim_image
        aim_image = aim_image = pygame.image.load("photos/celownik_1733_961.png")


class planets():

    def __init__(self,coords,name):
        self.cords = coords
        self.code = name

    def proximity(self,coords):
        if abs(coords[0] - self.cords[0] - 75) <= 60:
            if abs(coords[1] - self.cords[1] - 75) <= 60:
                return True
        return False

    def position(self):
        return self.cords

    def image(self):
        return self.image

    def shout_name(self):
        return self.code


def planet_choosing(planet_3_keys = False):

    loop = 1
    init_display()

    aim = crosshair()
    planet1 = planets((SCREEN_WIDTH*0.1,SCREEN_HEIGHT*0.2),"wenus")
    planet2 = planets((SCREEN_WIDTH*0.3,SCREEN_HEIGHT*0.4),"mars")
    planet3 = planets((SCREEN_WIDTH*0.7,SCREEN_HEIGHT*0.5),"jowisz")
    planet1_image = pygame.image.load("photos/planet1.png")
    planet2_image = pygame.image.load("photos/planet2.png")
    planet3_image = pygame.image.load("photos/planet3.png")
    choosen = False
    while loop:
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                loop = 0

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_s]:
            aim.move("S")
        if pressed[pygame.K_w]:
            aim.move("N")
        if pressed[pygame.K_a]:
            aim.move("W")
        if pressed[pygame.K_d]:
            aim.move("E")
        if pressed[pygame.K_e]:
            choosen = True

        if planet1.proximity(aim.position_on_map()):
            aim.green()
            if choosen:
                return 1
        elif planet2.proximity(aim.position_on_map()):
            aim.green()
            if choosen:
                return 2
        elif planet3.proximity(aim.position_on_map()):
            if planet_3_keys:
                aim.green()
                if choosen:
                    return 3
        else:
            aim.white()
            choosen = False

        screen.blit(background,(0, 0))
        if planet_3_keys:
            screen.blit(planet3_image,planet3.position())
        screen.blit(planet1_image,planet1.position())
        screen.blit(planet2_image,planet2.position())
        screen.blit(aim_image,aim.position_raw())
        pygame.display.update()
