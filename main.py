import pygame
import sys

from interface import Interface

class Main:
    def __init__(self):
        pygame.init()
        self.WINDOW_WIDTH = 800
        self.WIDOW_HEITGHT = 600
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WIDOW_HEITGHT))
        self.interface = Interface()

    def start(self):
        while True:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 0

    def draw(self):
        self.interface.draw(self.screen)
        pygame.display.update()


main = Main()
main.start()
