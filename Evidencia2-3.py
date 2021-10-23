import re

class Vehiculo():
    def __init__(self,unidad="",marca="",modelo="",km=int()):
        self.unidad = unidad
        self.marca = marca
        self.modelo = modelo
        self.km = km

    def recorrido(self,n):
        self.n = n + self.km

Alta = Vehiculo()
lista = []

while True:
    x = int(input("Cuantos vehiculos se van a dar de alta ?"))
    lista.append("ingrese la matricula de la unidad ")
