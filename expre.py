import re, datetime
class Persona():
    nacimiento = ""
    def __init__(self, nombre="" , apellido=""):
        self.nombre = nombre
        self.apellido = apellido

    def edad(self,fecha):
        dias = datetime.date.today() - self.nacimiento
        return int(dias.day /365)

p = persona("juan","peres")
print(p.nombre , p.apellido)