from math import pi
class circular_conantra:
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return pi*self.radio**2
    def longitud(self):
        return 2*pi*self.radio
x = float(input("Ingresa el radio del circulo "))
respuesta = circular_conantra (x)
print(f"El radio es {x}\nLa longitud es {respuesta.longitud()}\nEl area es {respuesta.area()}")