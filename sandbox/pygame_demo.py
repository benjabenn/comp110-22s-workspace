"""Pygame demo!"""

# Import and initialize the pygame library
from random import randint

import pygame

pygame.init()
 
# Set up the drawing window
screen = pygame.display.set_mode([800, 500])
                               
# pygame clock object controls tick rate
clock = pygame.time.Clock()
# Run until the user asks to quit
running = True
 
# (x, y, width, height)
rect: pygame.Rect = pygame.Rect(20, 20, 50, 50)
coins: list[pygame.Rect] = [pygame.Rect(200, 250, 25, 25), pygame.Rect(200, 400, 25, 25), pygame.Rect(200, 300, 25, 25)]
coin = pygame.Rect(200, 300, 25, 25)

while running:
    clock.tick(60)
 
    # Fill background
    screen.fill((120, 200, 255))

    # Draw rect (window, color(rgb), rect object)
    pygame.draw.rect(screen, (150, 10, 245), rect)

    # get_pos() gets the x,y position of the mouse and that is then offset by 25
    rect.x = pygame.mouse.get_pos()[0] - 25
    rect.y = pygame.mouse.get_pos()[1] - 25

    for coin in coins:
        pygame.draw.circle(screen, (235, 162, 52), (coin.centerx, coin.centery), 15)
        hit = coin.colliderect(rect)
        if hit:
            coins.remove(coin)

    # Checks every frame for any user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                coins.append(pygame.Rect(randint(100, 200), randint(200, 400), 25, 25))
   
    pygame.display.flip()
 
# Done! Time to quit.
pygame.quit()