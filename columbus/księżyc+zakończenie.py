import numpy as np
from functions import *
import pygame
from kolko_i_krzyzyk import tic_tac_toeing

def tygrys():
    tygrys = pygame.image.load('tygrys.jpeg')
    global screen
    screen = pygame.display.set_mode((600, 400))
    screen.blit(tygrys,(0,0))
    pygame.display.update()
    pygame.time.wait(3000)

def Ksiezyc():
    printing(['''Wiesz już, że kwiat paproci znajduje się na Księżycu. Udaj się tam.'''])
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
    tic_tac_toeing()
    printing(['''Wygrałeś!'''])
    printing(['''Widzisz przed sobą kwiat paproci. Może on zagwarantować
Ci wieczne szczęście, spełnić Twoje wszelkie marzenia
i dać Ci wszystko czego potrzebujesz.
Pamiętaj jednak, że żadną z tych rzeczy
nie możesz się podzielić.
Czy zerwiesz paproć, czy po tej męczącej
i niebezpiecznej podróży, wolisz zostawić sprawy takimi
jak się mają?'''])
    pygame.display.quit()
    print("Co wybierasz?")
    print("Odejdź bez paprotki - 1")
    print("Zerwij paproć - 2")
    wybor_konca = int(input())
    if wybor_konca == 1:
        printing(['''
            Zdecydowałeś/zdecydowałaś się odejść bez kwiatu paproci. Czy była to dobra decyzja?
            Trudno powiedzieć. Pamiętaj, że zawsze możesz spróbować go zdobyć przy następnej
            koniunkcji planet.'''])
        pygame.display.quit()
    else:
        cut_scene(['''Rok później'''])
        printing(['''Po zerwaniu kwiatu paproci osiadłeś/osiadłaś w wielkim
        pałacu, w którym wszystkie meble pokryte są złotem,
        nigdy nie brakuje jedzenia, które serwowane jest
        w postaci najbardziej znakomitych potraw,
        usługuje Ci kilkadziesiąt służących, a o czym pomyślisz,
        to staje się prawdą.'''])
        printing(['''Jesteś jednak bardzo samotny/samotna,
        nie mogłeś/mogłaś podzielić się niczym ze swoimi
        przyjaciółmi i rodziną. Pewnego dnia postanawiasz wyjść
        z pałacu i przejść się po pobliskiej wsi. Panuje w niej
        straszna bieda. W pewnym momencie dostrzegasz kilkuletnią
        dziewczynkę leżącą na drodze, drżącą z zimna i wychudzoną do kości.
        Wahasz się, bo bardzo chcesz jej pomóc, ale wiesz że wtedy,
        straciłbyś/straciłabyś całe swoje bogactwo.'''])
        pygame.display.quit()
        print("Co robisz?")
        print("Pomagasz dziewczynce - 1")
        print("Odchodzisz - 2")
        wybór_1 = int(input())
        if wybór_1 == 1:
            printing(['''Zdecydowałeś/zdecydowałaś się pomóc biednej dziewczynce.
        W mgnieniu oka Twój imponujący pałac górujący nad wsią znika,
        znikają twoje bogato obszyte ubrania
        i znajdujesz się sam/a na środku obcej wsi.
        Postanawiasz wrócić do swojej rodzinnej wsi.
        Boisz się, ale jednocześnie jest Ci jakoś lżej na sercu.'''])
        else:
            printing(['''Zdecydowałeś/zdecydowałaś się odejść.
        Wracasz do swojego pałacu, w którym to wszystkie meble
        pokryte są złotem, nigdy nie brakuje jedzenia
        i usługuje Ci kilkadziesiąt służących.
        Zasiadasz do stołu i zaczynasz zajadać się podanymi potrawami.
        Wszystko wydaje się w porządku, ale czujesz się bardzo samotnie
        i tak jakbyś tak naprawdę nic nie miał/a.'''])
        printing(['''Koniec.'''])


Ksiezyc()
