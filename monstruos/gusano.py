import random
from monstruo import Monstruo


class Gusano(Monstruo):

    def __init__(self):
        super().__init__(5, 2, 'gusano', 'gusano.png')
        self.rangoVision = 3
        self.chanceDeSeguir = 30
