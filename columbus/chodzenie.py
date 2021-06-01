import pygame, sys

def moving_background():
    screen.blit(bg_surface,(bg_x_pos, 0))
    screen.blit(bg_surface,(bg_x_pos + 0, 0))

def player():
    screen.blit(playerImg, (playerX, playerY))

pygame.init()
pygame.display.set_caption("Paprotnica")
screen = pygame.display.set_mode([580, 290])
clock = pygame.time.Clock()

x= 50
y= 210
width = 20
height = 20
vel = 5

bg_surface = pygame.image.load('gra/bg.jpg').convert()
bg_x_pos = 0

playerImg = pygame.image.load('gra/girl.png')
playerX = 30
playerY = 170

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    bg_x_pos -= 1
    moving_background()
    if bg_x_pos <= -580:
        bg_x_pos = 0

    player()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>0:
        x -= vel
    if keys[pygame.K_RIGHT] and x<500-width:
        x += vel


    pygame.display.update()
    clock.tick(50)

pygame.quit()
