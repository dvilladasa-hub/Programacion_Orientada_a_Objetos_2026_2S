class Planeta():
    def __init__(self, nombre, satelites, masa, volumen, diametro, distanciaalsol, observable, orbita,rotacion, tipolan):
        self.nombre=str(nombre)
        self.satelites=int(satelites)
        self.masa=float(masa)
        self.volumen=float(volumen)
        self.diametro=int(diametro)
        self.distanciaalsol=int(distanciaalsol)
        self.observable=bool(observable)
        self.orbita=float(orbita)
        self.rotacion=float(rotacion)
        self.tipoplaneta=str(tipolan)
    def calculardencidad(self):
        return(self.masa/self.volumen)
    def planetaexterior(self):
        if self.distanciaalsol > 508632758 :
            return True
        else:
            return False
    def imprimir(self):
        print(f"Nombre del planeta = {self.nombre}\nCantidad de satelites = {self.satelites}\nMasa del planeta = {self.masa}\nVolumen del planeta = {self.volumen}\nDiametro del planeta = {self.diametro}\nDistancia al sol = {self.distanciaalsol}\nTipo de planeta = {self.tipoplaneta}\nEs observable = {self.observable}\nPeriodo orbital = {self.orbita}\nPeriodo de rotacion = {self.rotacion}")
p1 = Planeta("Tierra", 1, 5973600000000000000000000, 1083210000000, 12742, 150000000, True, 1.0, 1.0, "TERRESTRE")
p2 = Planeta("Júpiter", 79, 1899000000000000000000000000, 1431300000000000, 139820, 750000000, True, 11.86, 0.41, "GASEOSO")
p1.imprimir()
print(f"Densidad del planeta = {p1.calculardencidad()}")
print(f"Es planeta exterior = {p1.planetaexterior()}\n")
p2.imprimir()
print(f"Densidad del planeta = {p2.calculardencidad()}")
print(f"Es planeta exterior = {p2.planetaexterior()}")
