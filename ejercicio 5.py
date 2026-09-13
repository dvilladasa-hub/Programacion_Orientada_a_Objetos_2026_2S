import math
class Calculos:
    def __init__(self, suma, x, y):
        self.suma = suma
        self.x = x
        self.y = y
    def calcular_x(self):
        return self.x + math.pow(self.y, 2)      
    def calcular_suma(self):
        suma_temporal = self.suma + self.x
        return suma_temporal + (self.calcular_x() / self.y)
suma_val = 0
x_val = 20
y_val = 40
respuesta = Calculos(suma_val, x_val, y_val)
print(f"Los resultados son:\nEl valor de x es : {respuesta.calcular_x()}\nEl valor de y es : {respuesta.y}\nEl valor de la suma es: {respuesta.calcular_suma()}")