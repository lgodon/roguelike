
import random

MUNDO_ANCHO = 64
MUNDO_ALTO = 36

TILE_VACIO = 0
TILE_PARED = 1
TILE_PISO = 2
TILE_PASILLO = 3

def crearNivel():
    nivel = [[0 for x in range(MUNDO_ALTO)] for y in range(MUNDO_ANCHO)]
    for columna in range(MUNDO_ANCHO):
        for fila in range(MUNDO_ALTO):
            nivel[columna][fila] = TILE_VACIO

    maxAnchoSala = MUNDO_ANCHO / 3 - 1
    maxAltoSala = MUNDO_ALTO / 3 -1

    crearSala(nivel, 5, 3, 18, 8)
    crearSala(nivel, 45, 3, 14, 10)
    crearSala(nivel, 7, 18, 15, 10)
    crearSala(nivel, 38, 22, 22, 14)

    crearPasilloHorizontal(nivel, 22, 46, 6)
    crearPasilloHorizontal(nivel, 21, 39, 24)
    crearPasilloVertical(nivel, 10, 10, 19)
    crearPasilloVertical(nivel, 50, 12, 23)

    return nivel

def crearSala(nivel, x, y, ancho, alto):

    # Paredes horizontales
    for i in range(ancho):
        nivel[x + i][y] = TILE_PARED
        nivel[x + i][y + alto - 1] = TILE_PARED

    # Paredes verticales
    for i in range(alto):
        nivel[x][y + i] = TILE_PARED
        nivel[x + ancho - 1][y + i] = TILE_PARED

    for i in range(1, ancho - 1):
        for j in range(1, alto - 1):
            nivel[x + i][y + j] = TILE_PISO

def crearPasilloHorizontal(nivel, x1, x2, y):

    for i in range(x1, x2):
        nivel[i][y] = TILE_PASILLO

def crearPasilloVertical(nivel, x, y1, y2):

    for i in range(y1, y2):
        nivel[x][i] = TILE_PASILLO
