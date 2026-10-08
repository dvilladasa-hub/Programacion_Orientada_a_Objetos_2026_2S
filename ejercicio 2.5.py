bd=[[],[],[],[],[],[]]
class CuentaBancaria:
    def __init__(self, Nombresdeltitular, Apellidosdeltitular, Numerodecuenta, Tipodecuenta,Saldo,EA):
        self.Nombresdeltitular=str(Nombresdeltitular)
        self.Apellidosdeltitular=str(Apellidosdeltitular)
        self.Numerodecuenta=int(Numerodecuenta)
        self.Tipodecuenta=Tipodecuenta
        self.Saldo=float(Saldo)
        self.ea=float(EA)
    def imprimir(self):
        pass
    def Consultarsaldo(self):
        print(f"Saldo de {self.Nombresdeltitular}: ${self.Saldo}")
    def consignar(self, Cantidad):
        if float(Cantidad) > 0:
            self.Saldo += float(Cantidad)
            print(f"Consignación realizada. Nuevo saldo: ${self.Saldo}")
        else:
            print("Cantidad inválida.")           
    def retirar(self, Cantidad):
        if 0 < float(Cantidad) <= self.Saldo:
            self.Saldo -= float(Cantidad)
            print(f"Retiro realizado. Nuevo saldo: ${self.Saldo}")
        else:
            print("Saldo insuficiente o cantidad inválida.")
    def compararcuentas(self, otra_cuenta):
        if self.Saldo >= otra_cuenta.Saldo:
            print(f"El saldo de {self.Nombresdeltitular} es mayor o igual al de {otra_cuenta.Nombresdeltitular}.")
        else:
            print(f"El saldo de {self.Nombresdeltitular} es menor al de {otra_cuenta.Nombresdeltitular}.")
    def transferencia(self, cuenta_destino, Cantidad):
        cantidad_num = float(Cantidad)
        if cuenta_destino.Numerodecuenta in bd[2]:
            if self.Saldo >= cantidad_num:
                self.Saldo -= cantidad_num          
                cuenta_destino.Saldo += cantidad_num 
                print(f"Transferencia de ${cantidad_num} realizada con éxito a {cuenta_destino.Nombresdeltitular}.")
            else:
                print("Operación inválida: Saldo insuficiente.")
        else:
            print("Operación inválida: Número de cuenta destino no encontrado en Base de Datos.")
    def aplicar_interes_mensual(self):
        valor_interes = self.Saldo * (self.ea / 100)
        self.Saldo += valor_interes
        print(f"Interés mensual del {self.ea}% aplicado. Nuevo saldo: ${self.Saldo}")
    #volvi los datos una tabla para hacer que transferencia funcione algo mas realista 
    def lista(self):
        bd[0].append(self.Nombresdeltitular)
        bd[1].append(self.Apellidosdeltitular)
        bd[2].append(self.Numerodecuenta)
        bd[3].append(self.Tipodecuenta)
        bd[4].append(self.Saldo)
        bd[5].append(self.ea)
cuenta1 = CuentaBancaria("Pedro", "Pérez", 123456789, "AHORROS", 100000.0, 1.5)
cuenta2 = CuentaBancaria("Luis", "León", 987654321, "CORRIENTE", 50000.0, 2.0)
cuenta1.lista()
cuenta2.lista()
cuenta1.transferencia(cuenta2, 30000)
cuenta1.Consultarsaldo()
cuenta2.Consultarsaldo()