from ficha import Ficha


class Cofre(Ficha):

    def __init__(self, x, y):
        super().__init__(x, y, 'Cofre', None)
        self.x = x
        self.y = y
        self.abierto = False

    def mover(self, tablero):
        # ¡El cofre no se mueve!
        pass

    def abrir(self):
        self.abierto = True
        
    def getImagen(self):
        if self.abierto == False:
            return 'cofre_cerrado.png'
        else:
            return 'cofre_abierto.png'
