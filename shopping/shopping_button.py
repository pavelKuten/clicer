import pygame


class ShoppingButton:
    def __init__(self):
        self.image = pygame.image.load('imgs/cross.png')
        self.pos = (0, 0)


    def draw(self, screen):
        screen.blit(self.image, self.pos)