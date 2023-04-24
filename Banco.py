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
            threading.Thread(target=banco.ingresar, args=(100,)).start()
        for i in range(20):
            threading.Thread(target=banco.ingresar, args=(50,)).start()
        for i in range(60):
            threading.Thread(target=banco.ingresar, args=(20,)).start()
        self.assertEqual(banco.saldo, 100 + 40 * 100 + 20 * 50 + 60 * 20)

    def test_retirar(self):
        banco = Banco()
        for i in range(40):
            threading.Thread(target=banco.retirar, args=(100,)).start()
        for i in range(20):
            threading.Thread(target=banco.retirar, args=(50,)).start()
        for i in range(60):
            threading.Thread(target=banco.retirar, args=(20,)).start()
        with self.assertRaises(ValueError):
            banco.retirar(10000)
        self.assertEqual(banco.saldo, 100 - 40 * 100 - 20 * 50 - 60 * 20)
        
    