# SATURN - Planeta nr. 2

print('Witaj na Saturnie. W oddali dostrzegasz coś na kształt lasu, który składa się z wielu kosmicznych roślin. '
      'Kilka z nich rozpoznajesz jako skrajnie niebezpieczne. Po zbliżeniu się, rozumiesz że, '
      'to co widzisz przed sobą to labirynt')
print('Przed wejściem do labiryntu dostrzegasz tabliczkę: “Witaj przybyszko! '
      'Aby uzyskać potrzebną Ci wskazówkę musisz przejść przez labirynt. '
      'Jest on niebezpieczny, także musisz pamiętać o przestrzeganiu tych zasad: '
      'kiedy znajdziesz się na rozstaju dróg zawsze skręcaj w lewo, '
      'nigdy nie oglądaj się za siebie, nie biegaj. Powodzenia!”. ')
print('Idziesz już jakiś czas przed siebie w labiryncie, aż w końcu '
      'dochodzisz do rozstaju dróg, w którą stronę pójdziesz?')
# Wybór_1: W prawo
# Wybór_2: W lewo
choice1 = input()
if choice1 == 'w prawo':
    print('Idziesz przed siebie, gdy nagle z krzaków wyskakuje na ciebie kosmiczny lew. '
          'Nie masz szans w starciu z tym drapieżnikiem. '
          'Chyba zapomniałeś/zapomniałaś, co było napisane na tabliczce przed labiryntem.')
# Umarłeś/umarłaś -> Powitanie

elif choice1 == 'w lewo':
    print('Tekst: Idziesz przed siebie, gdy nagle słyszysz za sobą kroki. '
          'Brzmią one jakby ktoś zbliżał się do Ciebie bardzo szybko.')
# Wybór_a: Oglądasz się za siebie, boisz się, że możesz zostać zaatakowany/zaatakowana od tyłu.
# Wybór_b: Postanawiasz nie oglądać się za siebie i uparcie iść do przodu.
    choice2 = input()
    if choice2 == 'wybór a':
        print('Gdy się odwracasz, widzisz przed sobą kosmiczną Meduzę, '
              'która swoim laserowym spojrzeniem zamienia Cię w kamień. '
              'Chyba zapomniałeś/zapomniałaś, co było napisane na tabliczce przed labiryntem.')
        # -> Umarłeś/umarłaś -> Powitanie')

    elif choice2 == 'wybór b':
        print('Tekst: Po paru chwilach nie słyszysz już za sobą kroków. '
              'Najwyraźniej musiała to być jedna z podpuch labiryntu. '
              'Idziesz dalej przed siebie, aż napotykasz na kolejny rozstaj dróg. W którą stronę pójdziesz?')
# Wybór_I: W prawo
# Wybór_II: W lewo

        choice3 = input()
        if choice3 == 'wybór I':
            print('Tekst: Idziesz przed siebie, po jakimś czasie orientujesz się, '
                  'że chodzisz w miejscu i nie możesz pójść dalej. '
                  'Po paru godzinach, z wyczerpania tracisz przytomność. '
                  'Chyba zapomniałeś/zapomniałaś, co było napisane na tabliczce przed labiryntem.')
            # -> Umarłeś/umarłaś -> Powitanie

        elif choice3 == 'wybór II':
            print('Wędrujesz już po labiryncie kilka godzin, wreszcie widzisz przed sobą coś co wygląda na wyjście. '
                  'Masz ochotę pobiec, aby w końcu wyjść z tego mrocznego miejsca. Co robisz?')
# Wybór_c: Biegniesz do wyjścia.
# Wybór_d: Spokojnie idziesz przed siebie.

            choice4 = input()
            if choice4 == 'wybór c':
                print('Niestety Twój bieg był bardzo głośny i '
                      'obudził krwiożercze stworzenia mieszkające na skraju labiryntu.'
                      '  Chyba zapomniałeś/zapomniałaś, co było napisane na tabliczce przed labiryntem.')
# -> Umarłeś/umarłaś -> Powitanie
            elif choice4 == 'wybór d':
                print('Udaje Ci się wyjść z labiryntu. '
                      'Na końcu znajduje się koperta z wskazówką dotyczącą położenia kwiatu paproci. '
                      'Wracasz do swojego statku kosmicznego. Odszyfruj wiadomość: -.- /… /../.  , i zapisz ją.')
                password = str(input())
                while password != 'ksie, Ksie, KSIE':
                    input('Nieprawidłowe hasło!: ')
                odp = input('Czy byłeś już na wszystkich planetach?')
                if odp == 'tak':
                    print('Znając już obie części wskazówki postaraj się je złączyć i wpisać do GPSa, '
                          'który pokieruje Cię na planetę, na której znajduje się kwiat paproci (użyj polskich znaków)')
                    password = str(input())
                    while password != 'księżyc, KSIĘŻYC, Księżyc':
                        input('Nieprawidłowe hasło!: ')
                    print('Wiesz już, że kwiat paproci znajduje się na Księżycu. Udaj się tam.')

                else:
                    print('Sprawdź na mapie, jak dolecieć na drugą planetę, '
                          'na której musisz znaleźć wskazówkę i udaj się tam.')
