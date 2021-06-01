import pygame
BLACK = (0,0,0)

def init_display():
    global screen,background
    screen = pygame.display.set_mode((1000,1000))
    background = pygame.Surface(screen.get_size())
    background.fill(BLACK)

class crosshair():

    def __init__(self):
        self.white()
        self.position = (500, 500)

    def move(self,dir):

        distance = 15
        if dir == "N":
            self.position = (self.position[0],self.position[1]-distance)
        if dir == "E":
            self.position = (self.position[0]+distance,self.position[1])
        if dir == "S":
            self.position = (self.position[0],self.position[1]+distance)
        if dir == "W":
            self.position = (self.position[0]-distance,self.position[1])
        self.even()

    def even(self):
        if self.position[0] < 10:
            self.position = (10,self.position[1])
        if self.position[0] > 990:
            self.position = (990,self.position[1])
        if self.position[1] < 10:
            self.position = (self.position[0],10)
        if self.position[1] > 990:
            self.position = (self.position[0],990)

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
    planet1 = planets((100,200),"wenus")
    planet2 = planets((300,400),"mars")
    planet3 = planets((700,500),"jowisz")
    planet1_image = pygame.image.load("photos/planet1.png")
    planet2_image = pygame.image.load("photos/planet2.png")
    planet3_image = pygame.image.load("photos/planet3.png")
    choosen = False
    while loop:
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                loop = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    aim.move("N")
                if event.key == pygame.K_RIGHT:
                    aim.move("E")
                if event.key == pygame.K_DOWN:
                    aim.move("S")
                if event.key == pygame.K_LEFT:
                    aim.move("W")
                if event.key == pygame.K_e:
                    choosen = True

        if planet1.proximity(aim.position_on_map()):
            aim.green()
            if choosen:
                print("lecimy na planetę 1")
                return
        elif planet2.proximity(aim.position_on_map()):
            aim.green()
            if choosen:
                print("lecimy na planetę 2")
                return
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

        screen.blit(background, (0, 0))
        """
        if paprociara ma oba elementy układanki:
            screen.blit(planet3_image,planet3.position())
        """
        screen.blit(planet1_image,planet1.position())
        screen.blit(planet2_image,planet2.position())

        screen.blit(aim_image,aim.position_raw())
        pygame.display.update()
