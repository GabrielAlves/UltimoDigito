from random import randint

class PotenciaAleatoria(object):
    def __init__(self):
        self.base = randint(1, 1000)
        self.expoente = randint(1, 1000)