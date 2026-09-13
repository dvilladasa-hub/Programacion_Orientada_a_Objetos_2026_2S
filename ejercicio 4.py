class Familia:
    def __init__(self, juan):
        self.juan = juan
    def alberto(self):    
        return 2/3 * self.juan
    def ana(self):
        return 4/3 * self.juan
    def mjuan(self):
        return self.juan + self.alberto() + self.ana()
juanedad=int(input())
respuesta= Familia(juanedad)
print(f"la edad de los familiares es:\nJuan =  {respuesta.juan}\nAlberto = {respuesta.alberto()}\nAna = {respuesta.ana()}\nMama de juan = {respuesta.mjuan()}")               