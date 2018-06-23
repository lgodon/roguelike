from asciimatics.screen import Screen
import mundo
import os

DIBUJO_JUGADOR = '@'
DIBUJO_PARED = '#'
DIBUJO_PISO = '.'
DIBUJO_PASILLO = '▒'

def iniciar():
    #Ajustamos el tamaño de la ventana
    #os.system('mode con: cols={} lines={}'.format(mundo.MUNDO_ANCHO, mundo.MUNDO_ALTO + 4))
    os.system('printf \'\e[8;{};{}t\''.format(mundo.MUNDO_ALTO + 4, mundo.MUNDO_ANCHO))
    global pantalla
    pantalla = Screen.open()

def getTecla():
    tecla = pantalla.get_key()
    while tecla == None:
        tecla = pantalla.get_key()
    return tecla

def borrarPantalla():
    pantalla.clear()

def dibujarJugador(x, y):
    pantalla.print_at(DIBUJO_JUGADOR, x, y)
    pantalla.refresh()

def dibujarMonstruo(monstruo):
    pantalla.print_at(monstruo.getAscii(), monstruo.getX(), monstruo.getY())
    pantalla.refresh()

def dibujarNivel(nivel):
    for columna in range(len(nivel)):
        for fila in range(len(nivel[columna])):
            dibujarTile(columna, fila, nivel[columna][fila])

    pantalla.refresh()

def dibujarTile(columna, fila, objeto):
    caracter = None

    if objeto == mundo.TILE_PARED:
        caracter = DIBUJO_PARED
    elif objeto == mundo.TILE_PISO:
        caracter = DIBUJO_PISO
    elif objeto == mundo.TILE_PASILLO:
        caracter = DIBUJO_PASILLO

    if caracter != None:
        pantalla.print_at(caracter, columna, fila)

def mostrarMensaje(mensajes):
    mensaje = ''
    for m in mensajes:
        if (len(mensaje) > 0):
            mensaje += ' - '
        mensaje += m
    pantalla.print_at(mensaje, 2, 42)
    pantalla.refresh()

def mostrarEstadisticas(jugador):
    pantalla.print_at('Vida: %d' % jugador.getVida(), 2, 43)
    pantalla.refresh()

def mostrarGameOver():
    pantalla.clear()
    #pantalla.print_at('Game Over', mundo.MUNDO_ANCHO / 2 - 5, mundo.MUNDO_ALTO / 2)
    pantalla.print_at('Game Over', 27, 20)
    pantalla.refresh()

def terminar():
    pantalla.close()
