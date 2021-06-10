wybor1 = True
wybor2 = True
wybor3 = True

print("Witaj na Planecie 1! Planetę, na której się znajdujesz pokrywają gęste chmury burzowe. Zdecyduj się, w którą stronę chcesz polecieć, w poszukiwaniu wskazówki.")
while wybor3:
    while wybor3:
        while wybor1:
            odp1 = input()
            if odp1 == "w lewo":
                wybor1 = False
            elif odp1 == "w prawo":
                print("Niestety zdaje się, że nic tu nie ma. Musisz zawrócić!")
                

        print("Coś wydaje się migać w oddali.")
        print("Gdy podlatujesz bliżej widzisz ogromnego sfinksa zbudowanego z brył z różnych materiałów i odpadów kosmicznych. Wskazówka znajduje się najprawdopodobniej wewnątrz sfinksa.")
        print("Witaj przybyszko, podejrzewam, że chciałabyś wejść do środka i zdobyć wskazówkę, która pomoże Ci w odnalezieniu kwiatu paproci. Aby to zrobić, musisz jednak rozwiązać zagadkę: Im więcej zabierasz, tym większe to się staje. Co to jest?")
        odp2 = input()
        if odp2 == "dziura" or odp2 == "Dziura" or odp2 == "DZIURA":
            print("Gratuluję, to prawidłowa odpowiedź, w nagrodę możesz wejść do środka i odebrać wskazówkę.")
            print("W środku sfinksa znalazłeś/znalazłaś zaszyfrowaną wiadomość, z częścią koordynatów planety, na której znajduje się kwiat. Odszyfruj wiadomość: --.. / -.-- / -.-.  , i zapisz ją")
            wybor2 = False
        else:
            print("Sfinks: “Niestety to nie jest prawidłowa odpowiedź”. Widzisz jak sfinks powstaje na swoich ogromnych łapach i uderza w Ciebie jedną z nich.")
            print("dead")

    odp3 = input()
    if odp3 == "zyc" or odp3 == "ZYC" or odp3 == "Zyc":
        print("Sprawdź na mapie, jak dolecieć na drugą planetę, na której musisz znaleźć wskazówkę i udaj się tam.")
        wybor3 = False
    else:
        print("probuj dalej")
print("Sprawdź na mapie, jak dolecieć na drugą planetę, na której musisz znaleźć wskazówkę i udaj się tam.")
    
