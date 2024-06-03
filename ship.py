import pygame

class Ship:
    def __init__(self, name):
        self.name = name

        self.x = 250
        self.y = 250

        # if name == 'ship1':
        #     self.image = pygame.image.load('ship1.png')

        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))

    def move_x(self, magnitude):
        self.x += magnitude
    
    def move_y(self, magnitude):
        self.y += magnitude
    
    def draw(self, win):
        win.blit(self.image, (self.x, self.y))