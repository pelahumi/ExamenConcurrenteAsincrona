import threading
import time
import random
import concurrent.futures

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
    
    def ganancias(self, numero):
        if self.estrategia == "numero concreto" and numero == self.n_apostado:
            self.saldo += self.apuesta * 10
        elif self.estrategia == "par o impar" and numero == self.n_apostado:
            self.saldo += self.apuesta * 2
        elif self.estrategia == "martingala" and numero == self.n_apostado:
            self.saldo += 360
        else:
            self.saldo -= self.apuesta
    
class Ruleta():
    def tirar(self):
        time.sleep(5) #Saca un número cada 5 segundos
        n = random.randint(0,36)
        return n

class Banca():
    def __init__(self):
        self.saldo = 50000
    

if __name__ == "__main__":
    ruleta = Ruleta()
    jugadores = []
    for i in range(4):
        jugador = Jugador("numero concreto", random.randint(0,36))
        jugadores.append(jugador)
    for i in range(4):
        jugador = Jugador("par o impar", )
        jugadores.append(jugador)
    for i in range(4):
        jugador = Jugador("martingala", random.randint(0,36))
        jugadores.append(jugador)

    for jugador in jugadores:
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            pool.map(jugador.apostar())
            pool.map(jugador.ganancias())

    
        
        



