from ficha import Ficha
from monstruo import Monstruo
from cofre import Cofre


class Jugador(Ficha):

    def __init__(self):
        super().__init__(8, 4, 'jugador', 'astronauta.png')
        self.vida = 200
        self.arma = None

    def asignarArma(self, arma):
        self.arma = arma

    def calcularDaño(self):
        if self.arma:
            return self.arma.daño
        else:
            return 1

    def pegar(self, jDaño):
        self.vida = self.vida - jDaño

    def getVida(self):
        return self.vida

    def mover(self, tablero):
        nx = self.x
        ny = self.y

        tecla = tablero.getTecla()

        if tecla == ord('d'):
            nx = nx + 1
        if tecla == ord('w'):
            ny = ny - 1
        if tecla == ord('a'):
            nx = nx - 1
        if tecla == ord('s'):
            ny = ny + 1

        if tablero.puedeMover(nx, ny):
            ficha = tablero.getFicha(nx, ny)

            if not ficha:
                # Nos movemos
                self.ubicar(nx, ny)
            else:

                if isinstance(ficha, Monstruo):
                    # Pegarle al monstruo
                    ficha.pegar(self.calcularDaño())
                    if ficha.estaMuerto():
                        tablero.agregarMensaje('Mataste al %s' % ficha.getNombre())
                    else:
                        tablero.agregarMensaje('Le pegaste al %s' % ficha.getNombre())

                elif isinstance(ficha, Cofre):
                    # Abrir el cofre
                    ficha.abrir(tablero)



