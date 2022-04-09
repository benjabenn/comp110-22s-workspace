"""BEE."""

import pygame
from pygame.locals import *
import random
import sys

pygame.init()

display = pygame.display.set_mode((600,600))

class falling(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.rect = pygame.Rect(random.randint(0, 600), random.randint(-1000, 0), 30, 30)

    def fall(self):
        self.rect.move_ip(0,1)
        if self.rect.top >= 800:
            self.rect.x = random.randint(0, 600)
            self.rect.y = random.randint(-1000, 0)


class player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.rect = pygame.rect(400, 400, 400, 400)


x = falling()
xs = [falling() for i in range(5)]
play = player()

while True:

    display.fill((255, 255, 255))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                play.rect.move_ip(-10, 0)
            elif i.key == pygame.K_RIGHT:
                play.rect.move_ip(10, 0)

    pygame.draw.rect(display, (10, 10, 10), x)
    x.fall()

    for i in xs:
        pygame.draw.rect(display, (10, 10, 10), i)
        i.fall()

    pygame.display.update()