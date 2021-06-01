import time
import os

def planeta_zero():

    # wstęp, myślę że fajnie gdyby wyświetlał się na środku ekranu
    print("""\
    Od wieków wszystkim wiadomo, że w jedyną taką noc w roku,
    kiedy to Księżyc, Ziemia, Jowisz i Saturn w koniunkcji staną,
    kwitnie paproć, a kto jej kwiatuszek znajdzie,
    urwie i schowa, ten wielkie na ziemi szczęście mieć będzie.
    Noc jednak ta jest bardzo krótka, a kwiat ten niezwykle ciężko znaleźć.
    Jest bardzo niepozorny, a droga do niego pełna jest zagadek i niebezpieczeństw.\
    """)

    print()

    # powitanie
    print("""\
    Witaj w grze [tytuł?].
    Wcielisz się w rolę [imię bohaterki],
    a Twoim zadaniem będzie podróż przez kosmiczne odmęty galaktyki
    w poszukiwaniu mistycznego kwiatu paproci.
    Uważaj jednak, droga ta jest niebezpieczna,
    a każdy najmniejszy błąd może kosztować Cię życie,
    które masz tylko jedno!
    Podejmuj rozważne decyzje i nie daj się zwieść!\
    """)

    print()

    # planeta zerowa
    while True:
        print("""\
    Aby wyruszyć w podróż, w poszukiwaniu kwiatu paproci
    musisz użyć swojego statku kosmicznego,
    który jednak wydaje się być uszkodzony.
    Zdecyduj, której części chcesz przyjrzeć się bliżej.\
        """)

        print()

        print("Zbiornik paliwa - wciśnij 1")
        print("Silnik - wciśnij 2")
        wybór_1 = int(input())
        if wybór_1 == 1:
            print("""\
    Zbiornik paliwa wydaje się być uszkodzony.
    Zdecyduj, która opcja naprawcza będzie najkorzystniejsza.\
            """)
            print("Załatanie zbiornika - wciśnij 1")
            print("Wymiana całego zbiornika na nowy - wciśnij 2")
            wybór_2 = int(input())
            if wybór_2 == 1:
                print("""\
    Załatanie zbiornika było dobrym wyborem.
    Uszkodzenie nie było na tyle poważne, aby wymieniać cały zbiornik.\
                """)
            else:
                print("""\
    Wymiana całego zbiornika na nowy, była bezsensownym wydatkiem.
    Załatanie zbiornika w zupełności by wystarczyło.
    No cóż, masz teraz mniej monet, ale przynajmniej nowy zbiornik.\
                """)
            print("Jednak nadal coś wydaje się być nie tak z silnikiem, czy chcesz się temu przyjrzeć?")
            print("Tak - wciśnij 1")
            print("Nie - wciśnij 2")
            wybór_3 = int(input())
            if wybór_3 == 1:
                print("""\
    Coś wydaje się być nie w porządku, jednakże nie za bardzo znasz się na budowie silnika statku kosmicznego.
    Czy chcesz poprosić o pomoc mechanika?\
                """)
                print("Tak - wciśnij 1")
                print("Nie - wciśnij 2")
                wybór_4 = int(input())
                if wybór_4 == 1:
                    print("""\
    Mechanik sprawdził i naprawił twój statek.
    Wyniosło Cię to dużo monet, ale dzięki temu jesteś pewien/pewna,
    że dolecimy do każdej planety bezpiecznie.\
                    """)
                else:
                    print("""\
    Jakimś cudem samemu udało Ci się naprawić usterkę.
    Dzięki temu zaoszczędziłeś/zaoszczędziłaś trochę monet,
    ale nie wiadomo, czy usterka jest naprawiona poprawnie.
    Miejmy nadzieję, że dolecisz na miejsce.\
                    """)
                break
            else:
                print("No to w drogę!")
                time.sleep(2)
                os.system("cls")
                print("Umarłeś_aś")
                print("""\
    Niestety uszkodzenia statku były zbyt poważne
    i przy starcie Twój statek kosmiczny stanął w płomieniach.
    Następnym razem wybieraj mądrze.\
                """)
                time.sleep(5)
                os.system("cls")
        else:
            print("""\
    Coś wydaje się być nie w porządku, jednakże nie za bardzo znasz się na budowie silnika statku kosmicznego.
    Czy chcesz poprosić o pomoc mechanika?\
            """)
            print("Tak - wciśnij 1")
            print("Nie - wciśnij 2")
            wybór_4 = int(input())
            if wybór_4 == 1:
                print("""\
    Mechanik sprawdził i naprawił twój statek.
    Wyniosło Cię to dużo monet, ale dzięki temu jesteś pewien/pewna,
    że dolecimy do każdej planety bezpiecznie.\
                """)
            else:
                print("""\
    Jakimś cudem samemu udało Ci się naprawić usterkę.
    Dzięki temu zaoszczędziłeś/zaoszczędziłaś trochę monet,
    ale nie wiadomo, czy usterka jest naprawiona poprawnie.
    Miejmy nadzieję, że dolecisz na miejsce.\
                """)
            print("Jednak nadal coś wydaje się być nie tak z zbiornikiem paliwa, czy chcesz się temu przyjrzeć?")
            print("Tak - wciśnij 1")
            print("Nie - wciśnij 2")
            wybór_5 = int(input())
            if wybór_5 == 1:
                print("""\
    Zbiornik paliwa wydaje się być uszkodzony.
    Zdecyduj, która opcja naprawcza będzie najkorzystniejsza.\
                """)
                print("Załatanie zbiornika - wciśnij 1")
                print("Wymiana całego zbiornika na nowy - wciśnij 2")
                wybór_2 = int(input())
                if wybór_2 == 1:
                    print("""\
    Załatanie zbiornika było dobrym wyborem.
    Uszkodzenie nie było na tyle poważne, aby wymieniać cały zbiornik.\
                    """)
                else:
                    print("""\
    Wymiana całego zbiornika na nowy, była bezsensownym wydatkiem.
    Załatanie zbiornika w zupełności by wystarczyło.
    No cóż, masz teraz mniej monet, ale przynajmniej nowy zbiornik.\
                    """)
                break
            else:
                print("No to w drogę!")
                time.sleep(2)
                os.system("cls")
                print("Umarłeś_aś")
                print("""\
    Niestety uszkodzenia statku były zbyt poważne
    i przy starcie Twój statek kosmiczny stanął w płomieniach.
    Następnym razem wybieraj mądrze.\
                """)
                time.sleep(5)
                os.system("cls")
