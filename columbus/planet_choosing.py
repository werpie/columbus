import pygame
from pygame.math import Vector2
BLACK = (0,0,0)
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
SCREEN_SIZE = (800,800)

def init_display():
    global screen,background
    screen = pygame.display.set_mode((SCREEN_SIZE))
    background = pygame.Surface(screen.get_size())
    background = pygame.image.load("photos/tlo.jpg")

class crosshair():

    def __init__(self):
        self.white()
        self.position = Vector2(SCREEN_HEIGHT/2, SCREEN_WIDTH/2)

    def move(self,dir):

        distance = 5
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


def planet_choosing():
    loop = 1
    init_display()
    aim = crosshair()
    planet1 = planets((SCREEN_WIDTH*0.1,SCREEN_HEIGHT*0.2),"wenus")
    planet2 = planets((SCREEN_WIDTH*0.3,SCREEN_HEIGHT*0.4),"mars")
    planet3 = planets((SCREEN_WIDTH*0.7,SCREEN_HEIGHT*0.5),"jowisz")
    planet1_image = pygame.image.load("photos/planet1.png")
    planet2_image = pygame.image.load("photos/planet2.png")
    planet3_image = pygame.image.load("photos/planet3.png")
    clocki = pygame.time.Clock()
    choosen = False
    while loop:
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                loop = 0

        #clocki.tick(30)
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
                print("lecimy na planetę 1")
                return 1
        elif planet2.proximity(aim.position_on_map()):
            aim.green()
            if choosen:
                print("lecimy na planetę 2")
                return 2
        else:
            """
            if paprociara ma oba elementy układanki
                if planet3.proximity(aim.position_on_map()):
                    aim.green()
            if choosen:
                print("lecimy na planetę 3")
                return
            else:
            """
            aim.white()
            choosen = False


        if planet3.proximity(aim.position_on_map()):
            aim.green()
            if choosen:
                print("lecimy na planetę 3")
                return

        screen.blit(background,(0, 0))
        """
        if paprociara ma oba elementy układanki:
            screen.blit(planet3_image,planet3.position())
        """
        screen.blit(planet1_image,planet1.position())
        screen.blit(planet2_image,planet2.position())
        screen.blit(aim_image,aim.position_raw())
        pygame.display.update()
