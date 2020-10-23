# Del archivo cajero1 se importa la clase Cajero
from cajero1 import Cajero
# Se crea la clase Banco
class Banco:
   # Se crea el metodo constructor
    def __init__(self):
        self.lista_cajeros = [] # se inicializa una lista vacia de nombre lista_cajeros
        #cajero_centro = Cajero(5000, "Centro")
        #self.lista_cajeros.append(cajero_centro)

    def crear_cajero(self, valor, nombre): # Se crea el metodo crear_cajero
        cajero_nuevo = Cajero(valor, nombre)# se crea la instancia cajero_nuevo
        self.lista_cajeros.append(cajero_nuevo) # se agrega cajero_nuevo en la lista_cajeros
        print("Se ha creado un nuevo cajero de manera exitosa")# se visualiza un string

    def retirar_dinero(self, valor, nombre):
        # Busca el cajero en self.lista_cajeros
        for cajero  in self.lista_cajeros:
            # compara el nombre del cajero en la lista, con el nombre asignado
            if cajero.nombre == nombre:
                # al cajero encontrado, le pasa el metodo retirar(de la clase Cajero)
                #  y entre parentesis el valor a retirar.
                saldo = cajero.retirar(valor)
                return saldo
    
    def consignar_dinero(self,valor, nombre):
        for cajero in self.lista_cajeros:
            if cajero.nombre == nombre:
                saldo = cajero.consignar(valor)
                return saldo

        