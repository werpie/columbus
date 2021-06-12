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

printing(['''
Od wieków wszystkim wiadomo, że w jedyną taką noc w roku,
kiedy to Księżyc, Ziemia, Jowisz i Saturn w koniunkcji staną,
kwitnie paproć, a kto jej kwiatuszek znajdzie,
urwie i schowa, ten wielkie na ziemi szczęście mieć będzie.
Noc jednak ta jest bardzo krótka, a kwiat ten niezwykle ciężko znaleźć.
Jest bardzo niepozorny, a droga do niego pełna jest zagadek
i niebezpieczeństw.''',
'''
Witaj w grze Kosmiczny Kwiat Paproci.
Wcielisz się w rolę Paprociary,
a Twoim zadaniem będzie podróż przez kosmiczne odmęty galaktyki
w poszukiwaniu mistycznego kwiatu paproci.
Uważaj jednak, droga ta jest niebezpieczna,
a każdy najmniejszy błąd może kosztować Cię życie,
które masz tylko jedno!
Podejmuj rozważne decyzje i nie daj się zwieść!'''])

while True:
    printing(['''
Aby wyruszyć w podróż, w poszukiwaniu kwiatu paproci
musisz użyć swojego statku kosmicznego,
który jednak wydaje się być uszkodzony.
Zdecyduj, której części chcesz przyjrzeć się bliżej.
'''])
    pygame.display.quit()
    print("Zbiornik paliwa - wciśnij 1")
    print("Silnik - wciśnij 2")
    wybór_1 = int(input())
    if wybór_1 == 1:
        printing(['''
Zbiornik paliwa wydaje się być uszkodzony.
Zdecyduj, która opcja naprawcza będzie najkorzystniejsza.
        '''])
        pygame.display.quit()
        print("Załatanie zbiornika - wciśnij 1")
        print("Wymiana całego zbiornika na nowy - wciśnij 2")
        wybór_2 = int(input())
        if wybór_2 == 1:
            printing(['''
Załatanie zbiornika było dobrym wyborem.
Uszkodzenie nie było na tyle poważne, aby wymieniać cały zbiornik.'''])
        else:
            printing(['''
Wymiana całego zbiornika na nowy, była bezsensownym wydatkiem.
Załatanie zbiornika w zupełności by wystarczyło.
No cóż, masz teraz mniej monet, ale przynajmniej nowy zbiornik.'''])
        printing(['''Jednak nadal coś wydaje się być nie
tak z silnikiem, czy chcesz się temu przyjrzeć?'''])
        pygame.display.quit()
        print("Tak - wciśnij 1")
        print("Nie - wciśnij 2")
        wybór_3 = int(input())
        if wybór_3 == 1:
            printing(['''
Coś wydaje się być nie w porządku,
jednakże nie za bardzo znasz się na budowie silnika statku kosmicznego.
Czy chcesz poprosić o pomoc mechanika?'''])
            pygame.display.quit()
            print("Tak - wciśnij 1")
            print("Nie - wciśnij 2")
            wybór_4 = int(input())
            if wybór_4 == 1:
                printing(['''
Mechanik sprawdził i naprawił twój statek.
Wyniosło Cię to dużo monet, ale dzięki temu jesteś pewien/pewna,
że dolecimy do każdej planety bezpiecznie.'''])
            else:
                printing(['''
Jakimś cudem samemu udało Ci się naprawić usterkę.
Dzięki temu zaoszczędziłeś/zaoszczędziłaś trochę monet,
ale nie wiadomo, czy usterka jest naprawiona poprawnie.
Miejmy nadzieję, że dolecisz na miejsce.'''])
            printing(['''No to w drogę!'''])
            break
        else:
            printing(['''No to w drogę!'''])
            time.sleep(2)
            os.system("cls")
            printing(['''Umarłeś_aś''',
'''
Niestety uszkodzenia statku były zbyt poważne
i przy starcie Twój statek kosmiczny stanął w płomieniach.
Następnym razem wybieraj mądrze.'''])
            time.sleep(5)
            os.system("cls")
    else:
        printing(['''
Coś wydaje się być nie w porządku,
jednakże nie za bardzo znasz się na budowie silnika statku kosmicznego.
Czy chcesz poprosić o pomoc mechanika?'''])
        pygame.display.quit()
        print("Tak - wciśnij 1")
        print("Nie - wciśnij 2")
        wybór_4 = int(input())
        if wybór_4 == 1:
            printing(['''
Mechanik sprawdził i naprawił twój statek.
Wyniosło Cię to dużo monet, ale dzięki temu jesteś pewien/pewna,
że dolecimy do każdej planety bezpiecznie.'''])
        else:
            printing(['''
Jakimś cudem samemu udało Ci się naprawić usterkę.
Dzięki temu zaoszczędziłeś/zaoszczędziłaś trochę monet,
ale nie wiadomo, czy usterka jest naprawiona poprawnie.
Miejmy nadzieję, że dolecisz na miejsce.''',
'''
Jednak nadal coś wydaje się być nie tak z zbiornikiem paliwa,
czy chcesz się temu przyjrzeć?'''])
        pygame.display.quit()
        print("Tak - wciśnij 1")
        print("Nie - wciśnij 2")
        wybór_5 = int(input())
        if wybór_5 == 1:
            printing(['''
Zbiornik paliwa wydaje się być uszkodzony.
Zdecyduj, która opcja naprawcza będzie najkorzystniejsza.'''])
            pygame.display.quit()
            print("Załatanie zbiornika - wciśnij 1")
            print("Wymiana całego zbiornika na nowy - wciśnij 2")
            wybór_2 = int(input())
            if wybór_2 == 1:
                printing(['''
Załatanie zbiornika było dobrym wyborem.
Uszkodzenie nie było na tyle poważne, aby wymieniać cały zbiornik.'''])
            else:
                printing(['''
Wymiana całego zbiornika na nowy, była bezsensownym wydatkiem.
Załatanie zbiornika w zupełności by wystarczyło.
No cóż, masz teraz mniej monet, ale przynajmniej nowy zbiornik.'''])
            printing(['''No to w drogę!'''])
            break
        else:
            printing(['''No to w drogę!'''])
            time.sleep(2)
            os.system("cls")
            printing(['''Umarłeś_aś''',
'''
Niestety uszkodzenia statku były zbyt poważne
i przy starcie Twój statek kosmiczny stanął w płomieniach.
Następnym razem wybieraj mądrze.'''])
            time.sleep(5)
            os.system("cls")
