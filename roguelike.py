import tiles
import tablero
from jugador import Jugador
from items.llave import Llave

def dibujarPantalla():
    tiles.borrarPantalla()
    tablero.dibujar()
    tiles.mostrarMensaje(tablero.getMensajes())
    tiles.mostrarEstadisticas(jugador)


jugador = Jugador()
#jugador.asignarArma(Llave())
tablero = tablero.Tablero(jugador)
tiles.iniciar()

dibujarPantalla()

while True:
    tecla = tiles.getTecla()

    if tecla:
        if chr(tecla) in ('X', 'x'):
            break

        if chr(tecla) in ('a', 's', 'd', 'w'):
            # Mover al jugador y al resto de las fichas
            tablero.mover(tecla)

        dibujarPantalla()

        if jugador.getVida() <= 0:
            # morir
            ascii.mostrarGameOver()
            break

tiles.terminar()
