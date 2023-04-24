#Importamos las librerías que necesitaremos
import threading
import unittest
import concurrent.futures

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

class TestBanco(unittest.TestCase):

    def test_simulacion(self):
        banco = Banco()

        with concurrent.futures.ThreadPoolExecutor(max_workers=40) as pool:
            pool.map(banco.ingresar, [100]*40)
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as pool:
            pool.map(banco.ingresar, [50]*20)
        with concurrent.futures.ThreadPoolExecutor(max_workers=60) as pool:
            pool.map(banco.ingresar, [20]*60)

        with concurrent.futures.ThreadPoolExecutor(max_workers=40) as pool:
            pool.map(banco.retirar, [100]*40)
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as pool:
            pool.map(banco.retirar, [50]*20)
        with concurrent.futures.ThreadPoolExecutor(max_workers=60) as pool:
            pool.map(banco.retirar, [20]*60)

        self.assertEqual(banco.saldo, 100)