class person():
    def __init__(self, nombre, apellido, documento, añonacimiento, genero, paisorigen):
        self.nombre = str(nombre)
        self.apellido = str(apellido)
        self.documento = str(documento)
        self.añonacimiento = int(añonacimiento)
        self.genero= str(genero)
        self.paisorigen= str(paisorigen)
    def imprimir (self):
        print(f"nombre = {self.nombre}\napellido = {self.apellido}\ndocumento = {self.documento}\naño de nacimento = {self.añonacimiento}\ngenero = {self.genero}\npais de nacimiento = {self.paisorigen}")
p1=person("Pedro","Perez","1053121010",2010,"M","Pais de las marabillas")
p1.imprimir()
p2 = person("Luis", "León", "1053223344", 2001, "H", "Colombia")
p2.imprimir()


