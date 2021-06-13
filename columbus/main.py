import pygame
from planet_choosing import planet_choosing
from klasy import *
from planeta_zero import *
from planeta1 import *
from kolko_i_krzyzyk import *
from Labirynt import *
from Paprociara import *
from chodzenie import *
from Zakonczenie import *
from Ksiezyc import *

def main():
    pygame.init()
    pygame.font.init()
    zero()
    loop = True
    while loop:
        temp = planet_choosing()
        if temp == 1:
            chodzenie()
            planeta1()
        if temp == 2:
            chodzenie()
            #wstep do labiryntu
            Labirynt()
    Ksiezyc()
if __name__ == '__main__':
    main()
