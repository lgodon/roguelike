from monstruo import Monstruo


class AlienK(Monstruo):

    def __init__(self):
        super().__init__(20, 5, 'Alien K', 'alienK.png')
        self.rangoVision = 5
        self.chanceDeSeguir = 30