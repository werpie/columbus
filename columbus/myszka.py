import pygame
import sys
screen = pygame.display.set_mode((1000, 500))
pygame.font.init()

def pierwszy_wybor():
    x = '''    Witaj na Saturnie. W oddali dostrzegasz coś na kształt lasu, który składa się z wielu kosmicznych roślin.
    Kilka z nich rozpoznajesz jako skrajnie niebezpieczne. Po zbliżeniu się, rozumiesz że, 
    to co widzisz przed sobą to labirynt
    Przed wejściem do labiryntu dostrzegasz tabliczkę: “Witaj przybyszko! 
    Aby uzyskać potrzebną Ci wskazówkę musisz przejść przez labirynt.
    Jest on niebezpieczny, także musisz pamiętać o przestrzeganiu tych zasad: 
    kiedy znajdziesz się na rozstaju dróg zawsze skręcaj w lewo, 
    nigdy nie oglądaj się za siebie, nie biegaj. Powodzenia!”. 
    Idziesz już jakiś czas przed siebie w labiryncie, aż w końcu 
    dochodzisz do rozstaju dróg, w którą stronę pójdziesz?'''.splitlines()

    font = pygame.font.SysFont('Times', 20)

    i = 0
    for index, line in enumerate(x):
        text = font.render(line, True, [255, 255, 255])
        screen.blit(text, (0, i))
        i += 20
        pygame.display.flip()


    wybor1 = pygame.Rect(20, 400, 20, 20)
    wybor2 = pygame.Rect(20, 450, 20, 20)
    pygame.draw.rect(screen, (0, 150, 255), wybor1, 3)
    pygame.draw.rect(screen, (0, 150, 255), wybor2, 3)
    text1 = font.render('w prawo', True, [255, 255, 255])
    screen.blit(text1, (50, 400))
    text2 = font.render('w lewo', True, [255, 255, 255])
    screen.blit(text2, (50, 450))
    pygame.display.flip()

    while True:
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if (450 < y < 470) and (20 < x < 40):
                    print('umarles')
                elif (400 < y < 420) and (20 < x < 40):
                    screen.fill((0,0,0))
                    drugi_wybor()

def drugi_wybor():
    x = '''    Idziesz przed siebie, gdy nagle słyszysz za sobą kroki.
    Brzmią one jakby ktoś zbliżał się do Ciebie bardzo szybko.'''.splitlines()

    font = pygame.font.SysFont('Times', 20)

    i = 0
    for index, line in enumerate(x):
        text = font.render(line, True, [255, 255, 255])
        screen.blit(text, (0, i))
        i += 20
        pygame.display.flip()

    wybor1 = pygame.Rect(20, 400, 20, 20)
    wybor2 = pygame.Rect(20, 450, 20, 20)
    pygame.draw.rect(screen, (0, 150, 255), wybor1, 3)
    pygame.draw.rect(screen, (0, 150, 255), wybor2, 3)
    text1 = font.render('Oglądasz się za siebie, boisz się, że możesz zostać zaatakowany/a od tyłu.',
                        True, [255, 255, 255])
    screen.blit(text1, (50, 400))
    text2 = font.render('Postanawiasz nie oglądać się za siebie i uparcie iść do przodu.', True, [255, 255, 255])
    screen.blit(text2, (50, 450))
    pygame.display.flip()

    while True:
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if (450 < y < 470) and (20 < x < 40):
                    print('dead')
                elif (400 < y < 420) and (20 < x < 40):
                    screen.fill((0, 0, 0))
                    trzeci_wybor()



def trzeci_wybor():
    x = '''    Po paru chwilach nie słyszysz już za sobą kroków.
    Najwyraźniej musiała to być jedna z podpuch labiryntu.
    Idziesz dalej przed siebie, aż napotykasz na kolejny rozstaj dróg. W którą stronę pójdziesz?'''.splitlines()

    font = pygame.font.SysFont('Times', 20)

    i = 0
    for index, line in enumerate(x):
        text = font.render(line, True, [255, 255, 255])
        screen.blit(text, (0, i))
        i += 20
        pygame.display.flip()

    wybor1 = pygame.Rect(20, 400, 20, 20)
    wybor2 = pygame.Rect(20, 450, 20, 20)
    pygame.draw.rect(screen, (0, 150, 255), wybor1, 3)
    pygame.draw.rect(screen, (0, 150, 255), wybor2, 3)
    text1 = font.render('w prawo', True, [255, 255, 255])
    screen.blit(text1, (50, 400))
    text2 = font.render('w lewo', True, [255, 255, 255])
    screen.blit(text2, (50, 450))
    pygame.display.flip()

    while True:
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if (450 < y < 470) and (20 < x < 40):
                    print('dead')
                elif (400 < y < 420) and (20 < x < 40):
                    screen.fill((0, 0, 0))
                    czwarty_wybor()


def czwarty_wybor():
    x = '''    Wędrujesz już po labiryncie kilka godzin, wreszcie widzisz przed sobą coś co wygląda na wyjście.
    Masz ochotę pobiec, aby w końcu wyjść z tego mrocznego miejsca. Co robisz?'''.splitlines()

    font = pygame.font.SysFont('Times', 20)

    i = 0
    for index, line in enumerate(x):
        text = font.render(line, True, [255, 255, 255])
        screen.blit(text, (0, i))
        i += 20
        pygame.display.flip()

    wybor1 = pygame.Rect(20, 400, 20, 20)
    wybor2 = pygame.Rect(20, 450, 20, 20)
    pygame.draw.rect(screen, (0, 150, 255), wybor1, 3)
    pygame.draw.rect(screen, (0, 150, 255), wybor2, 3)
    text1 = font.render('Biegniesz do wyjścia.', True, [255, 255, 255])
    screen.blit(text1, (50, 400))
    text2 = font.render('Spokojnie idziesz przed siebie.', True, [255, 255, 255])
    screen.blit(text2, (50, 450))
    pygame.display.flip()

    while True:
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if (450 < y < 470) and (20 < x < 40):
                    print('hello')
                elif (400 < y < 420) and (20 < x < 40):
                    print('hi')

pierwszy_wybor()








