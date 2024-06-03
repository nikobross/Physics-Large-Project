import pygame
from ship import Ship

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Space Ship")
win.fill((255, 255, 255))
pygame.draw.circle(win, (255, 0, 0), (250, 250), 75)
pygame.display.update()
clock = pygame.time.Clock()

ship1 = Ship("ship1")
speed = 5

running = True
while running:

    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        ship1.move_x(-speed)
    if keys[pygame.K_RIGHT]:
        ship1.move_x(speed)
    if keys[pygame.K_UP]:
        ship1.move_y(-speed)
    if keys[pygame.K_DOWN]:
        ship1.move_y(speed)


    win.fill((255, 255, 255))
    ship1.draw(win)

    pygame.display.update()

pygame.quit()