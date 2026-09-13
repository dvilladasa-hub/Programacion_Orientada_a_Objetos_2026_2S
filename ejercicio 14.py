class Potencia:
    def __init__(self, numero):
        self.numero = numero
    def cuadrado(self):
        return self.numero ** 2
    def cubo(self):
        return self.numero ** 3
x = float (input("Escriba el numero que quieres elevar al cuadrado y al cubo "))
respuesta = Potencia (x)
print(f"El numero base fue {x}\nEl numero elevado al cuadrado es {respuesta.cuadrado()}\nEl numero elevado al cubo es {respuesta.cubo()}")