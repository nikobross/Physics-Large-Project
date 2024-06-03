import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First Game")

win.fill((255, 255, 255))

pygame.draw.circle(win, (255, 0, 0), (250, 250), 75)

pygame.display.update()

clock = pygame.time.Clock()


running = True
while running:

    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.circle(win, (255, 0, 0), (250, 250), 75)

    pygame.display.update()

pygame.quit()