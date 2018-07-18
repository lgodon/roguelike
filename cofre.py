from ficha import Ficha
from random import randint
from items.llave import Llave


class Cofre(Ficha):

    def __init__(self, x, y):
        super().__init__(x, y, 'Cofre', None)
        self.x = x
        self.y = y
        self.abierto = False

    def mover(self, tablero):
        # ¡El cofre no se mueve!
        pass

    def abrir(self, tablero):
        if self.abierto:
            tablero.agregarMensaje('El cofre está vacio...')
            return

        self.abierto = True
        if randint(0, 100) < 75:
            arma = Llave()
            tablero.getJugador().asignarArma(arma)
            tablero.agregarMensaje('¡Conseguiste una %s!' % arma.nombre)
        else:
            tablero.agregarMensaje('El cofre está vacio...')
        
    def getImagen(self):
        if not self.abierto:
            return 'cofre_cerrado.png'
        else:
            return 'cofre_abierto.png'
