from ficha import Ficha
import random


class Monstruo(Ficha):

    def __init__(self, vida, daño, nombre, imagen):
        super().__init__(0, 0, nombre, imagen)
        self.rangoVision = 0
        self.chanceDeSeguir = 0
        self.daño = daño
        self.vida = vida

    def pegarAJ(self, tablero):
        jugador = tablero.getJugador()
        jugador.pegar(self.daño)
        tablero.agregarMensaje('Te pegó el %s (%d)' % (self.nombre, self.daño))

    def mover(self, tablero):
        # Si está al alcance, pegarle al jugador
        if self.estaJAlcance(tablero, 1):
            self.pegarAJ(tablero)
            return
        else:
            if self.estaJAlcance(tablero, self.rangoVision):
                # Si el monstruo ve al jugador, calcula las chances de seguirlo
                if random.randint(1, 100) <= self.chanceDeSeguir:
                    self.seguirAJ(tablero)

        return ''

    def estaJAlcance(self, tablero, distancia):
        jx = tablero.getJugador().getX()
        jy = tablero.getJugador().getY()

        if distancia >= jx - self.x >= -distancia and \
                distancia >= jy - self.y >= -distancia:
            return True
        else:
            return False

    def seguirAJ(self, tablero):
        jx = tablero.getJugador().getX()
        jy = tablero.getJugador().getY()
        mx = self.x
        if jx < self.x:
            mx = self.x - 1
        elif jx > self.x:
            mx = self.x + 1
        my = self.y
        if jy < self.y:
            my = self.y - 1
        elif jy > self.y:
            my = self.y + 1
        if tablero.puedeMover(mx, my) and not tablero.getFicha(mx, my):
            self.x = mx
            self.y = my

    def pegar(self, jDaño):
        self.vida = self.vida - jDaño

    def estaMuerto(self):
        if self.vida <= 0:
            return True
        else:
            return False
