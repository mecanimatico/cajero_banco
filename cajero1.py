class Cajero:

    def __init__(self, valor, nombre):
        self.estado = "vacio"
        self.valor = valor
        self.nombre = nombre

    def consignar(self, valor):
        self.valor += valor
        return "Valor consignado: ", + valor, "Nuevo saldo: ", self.valor

    def retirar(self, valor):
        if valor <= self.valor:
            self.valor -= valor
            return "Valor retirado: ", valor, "Nuevo saldo: ",self.valor
        else:
            return "Saldo insuficiente"

       