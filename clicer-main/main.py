import pygame
import sys

from interface import Interface
from boss import Boss


class Main:
    def __init__(self):
        pygame.init()
        self.WINDOW_WIDTH = 800
        self.WIDOW_HEITGHT = 600
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WIDOW_HEITGHT))
        self.interface = Interface()
        self.boss = Boss(1)
        self.player_damage = 6
        self.damage_per_second = 0

    def start(self):
        global event
        while True:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 0
                if event.type == pygame.MOUSEBUTTONUP:
                    self.try_to_click(event.pos)


    def draw(self):
        self.screen.fill((0, 0, 0))
        self.interface.draw(self.screen)
        self.interface.draw(self.screen)
        self.boss.draw(self.screen)
        self.draw_bar()
        pygame.display.update()

    def try_to_click(self, pos):
        if 100 < pos[0] < 700 and 200 < pos[1] < 600:
            self.interface.seed.count += self.boss.bite(self.player_damage)

    def draw_bar(self):
        k = self.boss.hp/(50 * self.boss.level)
        w = 400 * k
        pygame.draw.rect(self.screen, (0, 250, 0), (200, 100, int(w), 50), 0)


main = Main()
main.start()
