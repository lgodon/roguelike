import tiles
import mundo
from monstruos.gusano import Gusano
from monstruos.alienK import AlienK
from monstruos.enemergy import Enemergy
from cofre import Cofre


class Tablero:

    def __init__(self, jugador):
        self.fichas = []
        self.mensajes = []
        self.tecla = None
        self.nivel = mundo.crearNivel()
        self.fichas.append(jugador)
        self.agregarCofre(48, 4)
        self.agregarMonstruo(Gusano(), 7, 8)
        self.agregarMonstruo(Gusano(), 11, 6)
        self.agregarMonstruo(AlienK(), 10, 22)
        self.agregarMonstruo(Enemergy(), 11, 24)

    def dibujar(self):
        tiles.dibujarNivel(self.nivel)
        for ficha in self.fichas:
            tiles.dibujarFicha(ficha)

    def agregarMensaje(self, mensaje):
        self.mensajes.append(mensaje)

    def getMensajes(self):
        return self.mensajes

    def getTecla(self):
        return self.tecla

    def getJugador(self):
        return self.fichas[0]

    def getFicha(self, x, y):
        for ficha in self.fichas:
            if ficha.getX() == x and ficha.getY() == y:
                return ficha
        return None

    def agregarMonstruo(self, monstruo, x, y):
        monstruo.ubicar(x, y)
        self.fichas.append(monstruo)

    def agregarCofre(self, x, y):
        self.fichas.append(Cofre(x, y))

    def mover(self, tecla):
        self.mensajes = []
        self.tecla = tecla
        for ficha in self.fichas:
            if ficha.estaMuerto():
                self.fichas.remove(ficha)
            else:
                ficha.mover(self)

    def puedeMover(self, x, y):
        if self.nivel[x][y] in (mundo.TILE_PARED, mundo.TILE_VACIO):
            return False

        return True
