import re,datetime
class Clientes():
    
    def __init__(self,id,nombre,nacimiento):
        self.id = id
        self.nombre = nombre
        self.nacimiento = nacimiento
    
    def imprecion(self):
        pass
cosa = []

def Verificarid():
    print("Bienvenido al programa")
    while True:
        id = input("Ingrese una ID que contenga 8 digitos >>> ")
        if re.match("^\d{8}$",id):
            cosa.append(int(id))
            print("ID ,capturada")
            break
        else:
            print("id invalida, recuerde que su ID deve medir exactamente 8 caracteres")

def nombre():
    print("Bienvenido a la seccion de nombre ")
    while True:
        name = input("Ingrese un nombre Valido: ")
        if re.match(r"^.{5,30}$",name):
            cosa.append(str(name))
            print("Nombre capturado")
            break
        else:
            print("Nombre no valido \n Recuerde minimo 5 Maxico 30 caracteres")

def nacimiento():
    print("Bienvenido a la seccion de nacimiento")
    while True:
        nacimiento = input("Ingrese su fecha de nacimiento en el formato AAAA-MM-DD>>> ")
        if re.match(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$",nacimiento):
            anio=int(nacimiento[0:4])
            mes =int(nacimiento[5:7])
            dia =int(nacimiento[-2:])
            nacimiento = datetime.date(anio, mes, dia)
            cosa.append(nacimiento)
            return nacimiento  
        else:
            print("no esta en formato valido")

def main():
    Verificarid()
    nombre()
    nacimiento()
    print(cosa)
    input("oprima enter para cerrar el programa ")
    print("Adios")

import os,csv
kinko = []
def escribir():
    #primero informamos al usuario que se verificara si es la primera vez que se utiliza
     
    print("Bienvenido a Cargar informacion de usuario\n \n ")
    input("oprima enter para continuar>>>> ")
    if os.path.exists("individuos.csv"):
        with open("individuos.csv",newline="") as archivo_csv:
            lector_csv = csv.reader(archivo_csv, delimiter=',')
            for e in lector_csv:
               kinko.append(cosa(e[0],e[1],e[2]))
    else:
         archivo = open("individuos.csv","w")
         archivo.write("id,NOMBRE,NACIMIENTO")
         archivo.close()
    for o in kinko:
         print(o.correo)
         print(o.nombre)
         print(o.nacimiento)




        