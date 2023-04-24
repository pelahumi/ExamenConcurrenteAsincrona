#Importamos las librerías que necesitaremos
import threading

#Creamos la clase Banco
class Banco(threading.Thread):
    def __init__(self):
        super().__init__()
        self.saldo = 100
    
    def ingresar(self, cantidad_ingresar):
        if cantidad_ingresar == 100:
            self.saldo += cantidad_ingresar
            print("Se ingresaron 100 euros en su cuenta.")
        elif cantidad_ingresar == 50:
            self.saldo += cantidad_ingresar
            print("Se ingresaron 50 euros en su cuenta.")
        elif cantidad_ingresar == 20:
            self.saldo += cantidad_ingresar
            print("Se ingresaron 20 euros en su cuenta.")
        else:
            print("Error al ingresar el dinero.")

    def retirar(self, cantidad_retirar):
        if cantidad_retirar == 100:
            self.saldo += cantidad_retirar
            print("Se retiraron 100 euros en su cuenta.")
        elif cantidad_retirar == 50:
            self.saldo += cantidad_retirar
            print("Se retiraron 50 euros en su cuenta.")
        elif cantidad_retirar== 20:
            self.saldo += cantidad_retirar
            print("Se retiraron 20 euros en su cuenta.")
        else:
            print("Error al ingresar el dinero.")

    def run(self):
        pass
    