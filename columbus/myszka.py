import pygame
import sys
screen = pygame.display.set_mode((1000, 500))
pygame.font.init()


x = 'Witaj na Saturnie. Dokąd idziesz?'


font = pygame.font.SysFont('Times', 20)
text = font.render(x, True, [255, 255, 255])
screen.blit(text, (0, 0))

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
                print('hello')
            elif (400 < y < 420) and (20 < x < 40):
                print('hi')


