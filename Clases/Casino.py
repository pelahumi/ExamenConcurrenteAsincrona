import threading
import time
import random

class Jugador(threading.Thread):
    def __init__(self, estrategia, n_apostado, apuesta):
        self.saldo = 1000
        self.estrategia = estrategia
        self.n_apostado = n_apostado
        self.apuesta  = apuesta
        self.ultima_apuesta = False #True si ganó la última apuesta
    
    def apostar(self):
        if self.estrategia == "numero concreto":
            self.apuesta = 10
        elif self.estrategia == "par o impar":
            self.apuesta = 10
        elif self.estrategia == "martingala":
            if self.ultima_apuesta:
                self.apuesta *= 2
            else:
                self.apuesta = 10
        self.saldo -= self.apuesta
    
    def ganancias(self):
        


