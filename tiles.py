import pygame
import mundo

TILE_ANCHO = 20
TILE_ALTO = 20


def iniciar():
    global pantalla
    global texturas
    global fondo
    global piso
    global pared
    global fontPanel
    global fontGameOver
    global ancho
    global alto

    ancho = mundo.MUNDO_ANCHO * TILE_ANCHO
    alto = mundo.MUNDO_ALTO * TILE_ALTO + 100

    pantalla = pygame.display.set_mode([ancho, alto])
    pygame.display.set_caption('Roguelike!')

    pygame.key.set_repeat(200, 100)

    texturas = {}

    fondo = cargarImagen('fondo.png')
    piso = cargarImagen('piso.png')
    pared = cargarImagen('pared48.png')

    pygame.font.init()

    fontPanel = pygame.font.Font('resources/helvetica.ttf', 20)
    fontGameOver = pygame.font.Font('resources/bladerunner.ttf', 50)

def getTecla():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    return 120
                elif event.key == pygame.K_w:
                    return 119
                elif event.key == pygame.K_a:
                    return 97
                elif event.key == pygame.K_s:
                    return 115
                elif event.key == pygame.K_d:
                    return 100


def borrarPantalla():
    pass


def dibujarFicha(ficha):
    if not ficha.getImagen() in texturas:
        textura = cargarImagen(ficha.getImagen())
        texturas[ficha.getImagen] = textura
    else:
        textura = texturas[ficha.getImagen()]

    pantalla.blit(textura, (ficha.getX() * TILE_ANCHO, ficha.getY() * TILE_ALTO))
    pygame.display.update()


def dibujarNivel(nivel):
    for columna in range(len(nivel)):
        for fila in range(len(nivel[columna])):
            dibujarTile(columna, fila, nivel[columna][fila])

    pygame.display.update()


def dibujarTile(columna, fila, objeto):
    color = (0, 0, 0)
    tile = None

    if objeto == mundo.TILE_PARED:
        color = (120, 0, 0)
        tile = pared
    elif objeto == mundo.TILE_VACIO:
        tile = fondo
    elif objeto == mundo.TILE_PISO:
        color = (0, 120, 120)
        tile = piso
    elif objeto == mundo.TILE_PASILLO:
        color = (0, 0, 120)
        tile = piso

    if not tile:
        pygame.draw.rect(pantalla, color, (columna * TILE_ANCHO, fila * TILE_ALTO, TILE_ANCHO, TILE_ALTO))
    else:
        pantalla.blit(tile, (columna * TILE_ANCHO, fila * TILE_ALTO))


def mostrarMensaje(mensajes):
    mensaje = ''
    for m in mensajes:
        if len(mensaje) > 0:
            mensaje += ' - '
        mensaje += m
    pygame.draw.rect(pantalla, (0, 0, 0), (0, alto - 80, ancho, 40))
    if mensaje != '':
        texto = fontPanel.render(mensaje, True, (255, 255, 255))
        pantalla.blit(texto, (20, alto - 80))
    pygame.display.update()


def mostrarEstadisticas(jugador):
    texto = fontPanel.render('Vida: %d' % jugador.getVida(), True, (255, 255, 255))
    pygame.draw.rect(pantalla, (0, 0, 0), (0, alto - 40, ancho, 40))
    pantalla.blit(texto, (20, alto - 40))
    pygame.display.update()


def mostrarGameOver():
    pantalla.fill((0, 0, 0))
    texto = fontGameOver.render('Game over', True, (255, 0, 0))
    pantalla.blit(texto, (ancho / 2 - texto.get_rect().width / 2, alto / 2 - texto.get_rect().height / 2))
    pygame.display.update()


def terminar():
    pass


def cargarImagen(archivo):
    textura = pygame.image.load('pngs/' + archivo).convert_alpha()
    return pygame.transform.scale(textura, (TILE_ANCHO, TILE_ALTO))
