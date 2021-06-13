import pygame
from kolko_i_krzyzyk import tic_tac_toeing
from Zakonczenie import *
from functions import *

def tygrys():
    tygrys = pygame.image.load('photos/tygrys_mały.jpg')
    global screen
    screen = pygame.display.set_mode((600, 600))
    screen.blit(tygrys,(0,0))
    pygame.display.update()
    pygame.time.wait(3000)

def init_display():
    global screen,background
    screen = pygame.display.set_mode((1000,1000))
    background = pygame.Surface(screen.get_size())
    background.fill(pygame.image.load("C:\\repo\\git\\columbus\\columbus\\photos\\bg.jpg"))

class Ksiezyc(object):
    def __init__(self):
        #init_display()
        printing(['''Wiesz już, że kwiat paproci znajduje się na Księżycu. 
Udaj się tam.'''])
        cut_scene("Lecimy na Księżyc")
        printing(['''Witaj na Księżycu! 
To tutaj odnajdziesz mistyczny kwiat paproci,
który ma Ci zapewnić wieczne szczęście.'''])
        printing(['''Widzisz przed sobą miejsce, w którym znajduje się kwiat paproci.
Jednakże strzeże go kosmiczny Tygrys.'''])
        tygrys()
        printing(['''Aby go stamtąd przegonić, musisz
wygrać z nim w kółko i krzyżyk.'''])
        pygame.display.quit()
        temp = tic_tac_toeing()
        if temp == "computer":
            cut_scene("Przegrałeś i umierasz. :))))")
            pygame.quit()
            quit()
        printing(['''
    Widzisz przed sobą kwiat paproci. Może on zagwarantować
    Ci wieczne szczęście, spełnić Twoje wszelkie marzenia 
    i dać Ci wszystko czego potrzebujesz. 
    Pamiętaj jednak, że żadną z tych rzeczy 
    nie możesz się podzielić. 
    Czy zerwiesz paproć, czy po tej męczącej 
    i niebezpiecznej podróży, wolisz zostawić sprawy takimi 
    jak się mają?'''])
        pygame.display.quit()
        wybor_konca = int(input("Wybierz 1: Odejdź bez paprotki\nWybierz 2: Zerwij paproć"))
        if wybor_konca == 1:
            printing(['''
    Zdecydowałeś/zdecydowałaś się odejść bez kwiatu paproci. 
    Czy była to dobra decyzja? Trudno powiedzieć. 
    Pamiętaj, że zawsze możesz spróbować go zdobyć 
    przy następnej koniunkcji planet.'''])
        else:
            Zakonczenie()

