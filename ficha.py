class Ficha:

    def __init__(self, x, y, nombre, imagen):
        self.x = x
        self.y = y
        self.nombre = nombre
        self.imagen = imagen

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, nuevoX):
        self.x = nuevoX

    def setY(self, nuevoY):
        self.y = nuevoY

    def ubicar(self, x, y):
        self.x = x
        self.y = y

    def estaMuerto(self):
        return False

    def getNombre(self):
        return self.nombre

    def getImagen(self):
        return self.imagen

