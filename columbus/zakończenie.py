import pygame

def throwing_at_window(text,colour):
    """
    to mi potrzebne było do zabawy z printing
    """
    global font,screen
    font_size = 20
    pygame.font.init()
    font = pygame.font.SysFont("Times", font_size)
    text = text.splitlines()
    for index, line in enumerate(text):
        text1 = font.render(line, True, colour)
        screen.blit(text1, (0, index * font_size))
    pygame.display.update()

def printing(lista):
    """
    Do funkcji podajemy listę całych segmentów tekstu, które na ekran mają wlecieć naraz:
    ['''
    to sie pojawi na ekranie jako pierwsze i zniknie po kilku sekundach''',
    '''
    to sie pojawi drugie na ekranie i zniknie po kilku sekundach'''
    ]
    Miejsce na ekranie operujemy poprzez edycję łańcucha, spacje i entery

    Jeżeli chcemy zamknąć na chiwlę ekran, kiedy gracz ma coś wpisać do konsoli,
    to po użyciu funkcji używamy pygame.display.quit()
    """
    lista.append("end")
    global screen
    screen = pygame.display.set_mode((600, 400))
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    juz = True
    change = 10
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        if lista:
            if juz:
                juz = False
                text = lista[0]
                lista.pop(0)
                wt = 0


            white = (wt,wt,wt)
            screen.blit(background,(0,0))
            throwing_at_window(text,white)
            pygame.time.wait(100)
            wt +=change

            if wt>255:
                wt = 255
                change = 0

            if pygame.key.get_pressed()[pygame.K_e]:
                if wt == 255:
                    change = -20
                elif change>0:
                    wt = 230
                else:
                    wt = 0

            if wt< 0:
                wt = 0
                change = 10
                juz = True
                screen.blit(background,(0, 0))
        else:
            return

def zakończenie():
    printing(['''Rok później'''])
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
