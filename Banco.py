#Importamos las librerías que necesitaremos
import threading
import unittest

#Creamos la clase Banco
class Banco(threading.Thread):
    def __init__(self):
        self.saldo = 100
        self.bloquear = threading.Lock()
    
    def ingresar(self, cantidad_ingresar):
        self.bloquear.acquire()
        self.saldo += cantidad_ingresar
        self.bloquear.release()

    def retirar(self, cantidad_retirar):
        self.bloquear.acquire()
        if self.saldo < cantidad_retirar:
            raise ValueError("No hay suficiente dinero para retirar.")
        else:
            self.saldo -= cantidad_retirar
        self.bloquear.release()

class DockTestBanco(unittest.TestCase):
    def test_ingresar(self):
        banco = Banco()
        for i in range(40):
            threading.Thread(target=banco.retirar)
    