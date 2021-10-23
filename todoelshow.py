import re
class Producto():

    def __init__(self,nombre="", precio = 0.0):
        self.nombre = nombre
        self.precio = precio

    def iva(self):
        return self.precio * 0.16

def validareal(s):
    while True:
        num = input(s)
        if re.match( r'^[+]?\d*\.?\d*?$', num):
            return float(num)
        print("Debe ingresar un numero real")

b = validareal('Dime el precio')
print(b)
'''
a= Producto("Cocacola 500Ml",15.5)

print(a.nombre)
print(a.precio)
print(a.iva())
'''