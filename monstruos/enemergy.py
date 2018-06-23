from monstruo import Monstruo


class Enemergy(Monstruo):

    def __init__(self):
        super().__init__(5, 1, 'enemergy', 'blob.png')

    def mover(self, tablero):
        if self.estaJAlcance(tablero, 1):
            self.pegarAJ(tablero)
            return
        if tablero.puedeMover(self.x, self.y - 1):
            self.y = self.y - 1
