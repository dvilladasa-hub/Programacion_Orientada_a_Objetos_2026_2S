class Trabajador:
    def __init__(self, horas, vhora, porcentaje_retencion):
        self.h = horas
        self.vh = vhora
        self.p_rete = porcentaje_retencion
    def salario_bruto(self):
        return self.h*self.vh
    def retencion_en_la_fuente(self):
        return self.salario_bruto()*(self.p_rete/100)  
    def salario_neto(self):
        return self.salario_bruto()-self.retencion_en_la_fuente()
h1 = float(input("Ingrese las horas trabajadas "))
vh1 = float(input("Ingrese el valor de la hora "))
rete = float(input("Ingrese el valor del porcentaje de retencion en la fuente "))
trabajador = Trabajador(h1, vh1, rete)
print(f"El salario bruto es: {trabajador.salario_bruto()}\nLa retencion en la fuente es: {trabajador.retencion_en_la_fuente()}\nEl salario neto es: {trabajador.salario_neto()} ")