from item import Item


class Arma(Item):

    def __init__(self, nombre, daño):
        super().__init__(nombre)
        self.daño = daño
