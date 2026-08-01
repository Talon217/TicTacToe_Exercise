import pygame #noqa
import random

#pygame setup
pygame.init()
info = pygame.display.Info()
screen = pygame.display.set_mode(((info.current_w//2), (info.current_h//2)))
clock = pygame.time.Clock()
running = True



while running:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False

    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    screen.fill((r,g,b))

    pygame.display.flip()

    clock.tick(1) 
pygame.QUIT()
