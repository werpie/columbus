import pygame
BLACK = (0,0,0)

def init_display():
    global screen,background
    screen = pygame.display.set_mode((1000,1000))
    background = pygame.Surface(screen.get_size())
    background.fill(BLACK)

class Zakonczenie(object):
    def __init__(self):
        #init_display()
        print("Rok później")
        print("""\
            Po zerwaniu kwiatu paproci osiadłeś/osiadłaś w wielkim pałacu, w którym    
            wszystkie meble pokryte są złotem, nigdy nie brakuje jedzenia, które 
            serwowane jest w postaci najbardziej znakomitych potraw, usługuje Ci 
            kilkadziesiąt służących, a o czym pomyślisz, to staje się prawdą.
            """)
        print("""\
            Jesteś jednak bardzo samotny/samotna, nie mogłeś/mogłaś podzielić się 
            niczym ze swoimi przyjaciółmi i rodziną. Pewnego dnia postanawiasz wyjść 
            z pałacu i przejść się po pobliskiej wsi. Panuje w niej straszna bieda. 
            W pewnym momencie dostrzegasz kilkuletnią dziewczynkę leżącą na drodze, 
            drżącą z zimna i wychudzoną do kości. Wahasz się, bo bardzo chcesz jej pomóc, 
            ale wiesz że wtedy, straciłbyś/straciłabyś całe swoje bogactwo. Co robisz?
            """)
        wybor_konca = int(input("Wybierz 1: Pomagasz dziewczynce\nWybierz 2: Odchodzisz"))
        if wybor_konca == 1:
            print("""\
                Zdecydowałeś/zdecydowałaś się pomóc biednej dziewczynce. W mgnieniu oka Twój 
                imponujący pałac górujący nad wsią znika, znikają twoje bogato obszyte ubrania 
                i znajdujesz się sam/a na środku obcej wsi. Postanawiasz wrócić do swojej rodzinnej 
                wsi. Boisz się, ale jednocześnie jest Ci jakoś lżej na sercu.
                """)
        else:
            print("""\
                Zdecydowałeś/zdecydowałaś się odejść. Wracasz do swojego pałacu, w którym to wszystkie
                meble pokryte są złotem, nigdy nie brakuje jedzenia i usługuje Ci kilkadziesiąt służących. 
                Zasiadasz do stołu i zaczynasz zajadać się podanymi potrawami. Wszystko wydaje się w porządku, 
                ale czujesz się bardzo samotnie i tak jakbyś tak naprawdę nic nie miał/a.
                """)




