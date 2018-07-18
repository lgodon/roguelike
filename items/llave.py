from arma import Arma


class Llave(Arma):

    def __init__(self):
        super().__init__('llave inglesa', 2)

    def getDescripcion(self):
        return 'La mejor amiga de los ingenieros'
