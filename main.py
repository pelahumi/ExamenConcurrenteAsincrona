from Banco import *

if __name__ == "__main__":
    banco =  Banco()
    with multiprocessing.Pool() as pool:
        pool.map(banco.ingresar(100),range(0,40))
    print("EL saldo final:",banco.saldo)
