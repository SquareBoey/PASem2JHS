import re
tasa_iva = 0.16
class Producto():
    existencia = 0
    def __init__(self, nombre='', precio=0.0):
        self.nombre = nombre
        self.precio = precio
        
    def iva(self):
        return self.precio * tasa_iva

    def entrada(self, cant):
        self.existencia += cant

    def salida(self, cant):
        if self.existencia >= cant:
            self.existencia -= cant
        else:
            print('No se cuenta con existencias suficientes.')
            cant = validaentero('Cantidad de unidades vendidas: ')
            self.salida(cant)

def validareal(s):
    while True:
        num = input(s)
        if re.match(r'^[+]?\d*\.?\d*([E|e][+|-]?\d*)?$', num):
            return float(num)
        print('Debe ingresar un número real positivo.')

def validaentero(s):
    while True:
        num = input(s)
        if re.match(r'^[+]?\d+$', num):
            return int(num)
        print('Debe ingresar un número entero positivo.')