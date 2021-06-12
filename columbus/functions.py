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

def cut_scene(tekst):
    """
    Funkcja działa tak, że podajesz jej tekst, a ona wyświetla go na ekranie
    Ma służyć jako przerywnik pomiędzy poszczególnymi segmentami
    Typu wybrana została planeta nr 1 to wpisujemy "Lecimy na planete nr 1"
    Pojawia się ekranik i znika po kilku sekundach
    """

    screen_size = (600,400)
    screen = pygame.display.set_mode(screen_size)
    background = pygame.Surface(screen.get_size())
    background.fill((0,0,0))
    screen.blit(background,(0,0))
    font = pygame.font.SysFont("Times",40)
    wt = 0
    loop = True
    change = 8
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        text = font.render(tekst,True,(wt,wt,wt))
        text_size = text.get_size()
        screen.blit(background, (0, 0))
        screen.blit(text,((600 - text_size[0])/2,(400 - text_size[1])/2))
        pygame.display.update()
        pygame.time.wait(100)
        wt += change
        if wt>240:
            change = -8
        if wt<0:
            return
