import pygame
from kolko_i_krzyzyk import tic_tac_toeing
import Zakonczenie

def init_display():
    global screen,background
    screen = pygame.display.set_mode((1000,1000))
    background = pygame.Surface(screen.get_size())
    background.fill(pygame.image.load("C:\\repo\\git\\columbus\\columbus\\photos\\bg.jpg"))

class Ksiezyc(object):
    def __init__(self):
        #init_display()
        print("Wiesz już, że kwiat paproci znajduje się na Księżycu. Udaj się tam.")
        print("Witaj na Księżycu! To tutaj odnajdziesz mistyczny kwiat paproci, który ma Ci zapewnić wieczne szczęście. ")
        tic_tac_toeing()
        print("""\
            Widzisz przed sobą kwiat paproci. Może on zagwarantować Ci wieczne szczęście, 
            spełnić Twoje wszelkie marzenia i dać Ci wszystko czego potrzebujesz. Pamiętaj 
            jednak, że żadną z tych rzeczy nie możesz się podzielić. Czy zerwiesz paproć, 
            czy po tej męczącej i niebezpiecznej podróży, wolisz zostawić sprawy takimi jak 
            się mają?
            """)
        wybor_konca = int(input("Wybierz 1: Odejdź bez paprotki\nWybierz 2: Zerwij paproć"))
        if wybor_konca == 1:
            print("""\
                Zdecydowałeś/zdecydowałaś się odejść bez kwiatu paproci. Czy była to dobra decyzja?    
                Trudno powiedzieć. Pamiętaj, że zawsze możesz spróbować go zdobyć przy następnej 
                koniunkcji planet.""")
        else:
            Zakonczenie()




