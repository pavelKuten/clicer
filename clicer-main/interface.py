from PAVEL.seed import Seed
from PAVEL.name import Name
from PAVEL.level import Level
from PAVEL.shop_button import ShopButton

class Interface:
    def __init__(self):
        self.shop_button = ShopButton()
        self.level = Level()
        self.name = Name()
        self.seed = Seed()

    def draw(self, screen):
        self.shop_button.draw(screen)
        self.seed.draw(screen)
        self.name.draw(screen)
        self.level.draw(screen)