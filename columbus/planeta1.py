import pygame
import time
import os

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

wybor1 = True
wybor2 = True
wybor3 = True

#problem jest taki, że przy śmierci cofamy się do "coś miga w oddali", a nie do samego początku

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
