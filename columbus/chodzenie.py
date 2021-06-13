import pygame, sys

def chodzenie(back):
    pygame.init()
    pygame.display.set_caption("Paprotnica")
    screen = pygame.display.set_mode([580, 290])
    clock = pygame.time.Clock()
    pygame.draw.line(screen,(0,0,0),(100,170),(100,110),10)
    x = 300
    if back == 1:
        bg_surface = pygame.image.load('photos/bg.jpg').convert()
        bg_size = 588
    else:
        bg_surface = pygame.image.load('photos/doom_bg_smoool.jpg').convert()
        bg_size = 757
    bg_x_pos = 0

    playerImg = pygame.image.load('photos/girl.png')
    playerX = 30
    playerY = 170

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_a]:
            bg_x_pos += 5
            x +=5
        if pressed[pygame.K_d]:
            bg_x_pos -= 5
            x -=5


        #bg_x_pos -= 1
        screen.blit(bg_surface,(bg_x_pos, 0))
        screen.blit(bg_surface,(bg_x_pos+bg_size,0))
        screen.blit(bg_surface,(bg_x_pos-bg_size, 0))
        pygame.draw.line(screen, (0, 0, 0), (x, 170),(x, 240), 10)
        screen.blit(playerImg, (playerX, playerY))
        pygame.display.update()
        clock.tick(50)
        if playerX+65==x:
            return
