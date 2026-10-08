from enum import Enum
class TipoA(Enum):
    CIUDAD = "CIUDAD"
    SUBCOMPACTO = "SUBCOMPACTO"
    COMPACTO = "COMPACTO"
    FAMILIAR = "FAMILIAR"
    EJECUTIVO = "EJECUTIVO"
    SUV = "SUV"
class TipoColor(Enum):
    BLANCO = "BLANCO"
    NEGRO = "NEGRO"
    ROJO = "ROJO"
    NARANJA = "NARANJA"
    AMARILLO = "AMARILLO"
    VERDE = "VERDE"
    AZUL = "AZUL"
    VIOLETA = "VIOLETA"
class TipoCom(Enum):
    GASOLINA = "GASOLINA"
    BIOETANOL = "BIOETANOL"
    DIESEL = "DIESEL"
    BIODIESEL = "BIODIESEL"
    GAS_NATURAL = "GAS_NATURAL"
class Automovil:
    VALOR_POR_MULTA = 100.0
    def __init__(self, marca: str, modelo: int, motor: int,
                 tipo_combustible: TipoCom, tipo_automovil: TipoA,
                 numero_puertas: int, cantidad_asientos: int,
                 velocidad_maxima: int, color: TipoColor, 
                 es_automatico: bool = False):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_automovil = tipo_automovil
        self.numero_puertas = numero_puertas
        self.cantidad_asientos = cantidad_asientos
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self.es_automatico = es_automatico
        self.velocidad_actual = 0
        self.cantidad_multas = 0 
    def get_es_automatico(self) -> bool:
        return self.es_automatico
    def set_es_automatico(self, es_automatico: bool):
        self.es_automatico = es_automatico
    def acelerar(self, incremento_velocidad: int):
        if self.velocidad_actual + incremento_velocidad <= self.velocidad_maxima:
            self.velocidad_actual += incremento_velocidad
        else:
            self.cantidad_multas += 1
            print(f"INFRACCIÓN: Supera la velocidad máxima permitida ({self.velocidad_maxima} km/h). "
                  f"Se genera una multa (Total multas: {self.cantidad_multas}).")
    def desacelerar(self, decremento_velocidad: int):
        if (self.velocidad_actual - decremento_velocidad) >= 0:
            self.velocidad_actual -= decremento_velocidad
        else:
            print("No se puede decrementar a una velocidad negativa.")
    def frenar(self):
        self.velocidad_actual = 0
    def calcular_tiempo_llegada(self, distancia: int) -> float:
        if self.velocidad_actual == 0:
            return float('inf')
        return distancia / self.velocidad_actual
    def tiene_multas(self) -> bool:
        return self.cantidad_multas > 0
    def obtener_total_multas(self) -> float:
        return self.cantidad_multas * self.VALOR_POR_MULTA
    def imprimir(self):
        print(f"Marca = {self.marca}")
        print(f"Modelo = {self.modelo}")
        print(f"Motor = {self.motor}")
        print(f"Tipo de combustible = {self.tipo_combustible.value}")
        print(f"Tipo de automóvil = {self.tipo_automovil.value}")
        print(f"Número de puertas = {self.numero_puertas}")
        print(f"Cantidad de asientos = {self.cantidad_asientos}")
        print(f"Velocidad máxima = {self.velocidad_maxima}")
        print(f"Color = {self.color.value}")
        print(f"Es automático = {'Sí' if self.es_automatico else 'No'}")
if __name__ == "__main__":
    auto1 = Automovil("Ford", 2018, 3, TipoCom.DIESEL, TipoA.EJECUTIVO, 5, 6, 250, TipoColor.NEGRO, True)
    auto1.imprimir()
    print("-" * 40)
    auto1.acelerar(100)
    print(f"Velocidad actual = {auto1.velocidad_actual} km/h")
    auto1.acelerar(120)
    print(f"Velocidad actual = {auto1.velocidad_actual} km/h")  
    auto1.acelerar(50)  
    auto1.acelerar(40) 
    print("-" * 40)
    print(f"¿Tiene multas el vehículo?: {auto1.tiene_multas()}")
    print(f"Cantidad de infracciones: {auto1.cantidad_multas}")
    print(f"Valor total de las multas: ${auto1.obtener_total_multas():.2f}")