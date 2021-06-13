import pygame
from planet_choosing import planet_choosing
from planeta_zero import *
from planeta1 import *
from Labirynt import *
from chodzenie import *
from Ksiezyc import *
from myszka import *

def main():
    pygame.init()
    pygame.font.init()
    zero()
    loop = True
    temp1 = [0,0,0]
    while loop:
        if sum(temp1) == 3:
            temp = planet_choosing(True)
        else:
            temp = planet_choosing()
        if temp == 1:
            if temp1[0] == 0:
                chodzenie(1)
                Jowisz()
                cut_scene("Znaleźliśmy pierwszą część koordynatów Planety")
                cut_scene("Wsiadamy s powrotem do s tatku!")
                temp1[0] = 1
            else:
                cut_scene("Już byliśmy na tej planecie, wybierz inną :))")
        if temp == 2:
            if temp1[1] == 0:
                chodzenie(2)
                #wstep do labiryntu
                Game()
                cut_scene("Znaleźliśmy drugą część koordynatów Planety")
                cut_scene("Wsiadamy spowrotem do statku!")
                temp1[1] = 1
            else:
                cut_scene("Już byliśmy na tej planecie, wybierz inną :))")
        if temp == 4:
            if temp1[2] == 0:
                pierwszy_wybor()
                cut_scene("Znaleźliśmy trzecią część koordynatów Planety")
                cut_scene("Wsiadamy spowrotem do statku!")
                temp1[2] = 1
            else:
                cut_scene("Już byliśmy na tej planecie, wybierz inną :))")
        if temp == 3:
            Ksiezyc()
            loop = False

    printing(["użyte obrazki:google :)"])

if __name__ == '__main__':
    main()
