import numpy as np
import pygame
import time
import os
from functions import *

def sfinks():
    sfinks = pygame.image.load('photos/sfinks.jpg')
    global screen
    screen = pygame.display.set_mode((600, 400))
    screen.blit(sfinks,(0,0))
    pygame.display.update()
    pygame.time.wait(3000)

#problem jest taki, że przy śmierci cofamy się do "coś miga w oddali", a nie do samego początku

def Jowisz():
    wybor1 = True
    wybor2 = True
    wybor3 = True
    printing(['''Witaj na Jowiszu!
Planetę, na której się znajdujesz pokrywają gęste chmury burzowe.
Zdecyduj się, w którą stronę chcesz polecieć, w poszukiwaniu wskazówki.'''])
    pygame.display.quit()
    print("W lewo - 1")
    print("W prawo - 2")
    while True:
        while wybor3:
            while wybor2:
                while wybor1:
                    odp1 = int(input())
                    if odp1 == 1:
                        wybor1 = False
                    elif odp1 == 2:
                        print("Niestety zdaje się, że nic tu nie ma. Musisz zawrócić!")


                printing(['''Coś wydaje się migać w oddali.'''])
                printing(['''Gdy podlatujesz bliżej widzisz ogromnego sfinksa
zbudowanego z brył z różnych materiałów i odpadów kosmicznych.
Wskazówka znajduje się najprawdopodobniej wewnątrz sfinksa.'''])
                sfinks()
                printing(['''Witaj przybyszko, podejrzewam, że chciałabyś wejść do środka
i zdobyć wskazówkę, która pomoże Ci w odnalezieniu kwiatu paproci.
Aby to zrobić, musisz jednak rozwiązać zagadkę:
Im więcej zabierasz, tym większe to się staje.'''])
                pygame.display.quit()
                print("Co to jest?")
                odp2 = input()
                if odp2 == "dziura" or odp2 == "Dziura" or odp2 == "DZIURA":
                    printing(['''Gratuluję, to prawidłowa odpowiedź,
w nagrodę możesz wejść do środka i odebrać wskazówkę.'''])
                    printing(['''W środku sfinksa znalazłeś/znalazłaś zaszyfrowaną wiadomość,
z częścią koordynatów planety, na której znajduje się kwiat.
Odszyfruj wiadomość: --.. / -.-- / -.-.  , i zapisz ją:'''])
                    wybor2 = False
                    pygame.display.quit()
                    break
                else:
                    printing(['''Sfinks: “Niestety to nie jest prawidłowa odpowiedź”.
Widzisz jak sfinks powstaje na swoich ogromnych łapach
i uderza w Ciebie jedną z nich.'''])
                    time.sleep(2)
                    os.system("cls")
                    printing(['''Umarłeś_aś'''])

            print("Zapisz odszyfrowaną wiadomość:")
            odp3 = input()
            if odp3 == "zyc" or odp3 == "ZYC" or odp3 == "Zyc":
                printing(['''Dobrze odszyfrowałeś/odszyfrowałaś wiadomość.''',
'''Sprawdź na mapie, jak dolecieć na drugą planetę,
na której musisz znaleźć kolejną wskazówkę i udaj się tam.'''])
                wybor3 = False
                pygame.display.quit()
            else:
                print("Próbuj dalej")