import re,datetime,csv

def getCaducidad():
        while True:
            cosa = open("lote.csv","a+")
            try:
                caducidad = input("Fecha de caducidad (aaaa-mm-dd): ")
                if (caducidad ==""):
                    print("La fecha de caducidad no se puede omitir.")
                else:
                    if (re.match(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", caducidad)):
                        cosa.write(caducidad)
                        cosa.write(",")
                        cosa.close()
                        print("La caducidad es de: ")
                        anio=int(caducidad[0:4])
                        mes=int(caducidad[5:7])
                        dia=int(caducidad[-2:])
                        caducidad = datetime.date(anio, mes, dia)
                        return caducidad
                    else:
                        print("El dato no está en formato aaaa-mm-dd.")
            except ValueError:
                print("La fecha no es una fecha válida.")

def clave():
    while True:
        cosa = open("lote.csv","a+")
        pregunta = input("Ingrese un codigo con el siguiente formato AAA-123 : ")
        if pregunta =="":
            print("No se puede omitir este campo")
        elif (re.match("^[A-Z]{3}-[0-9]{3}$", pregunta)):
            cosa.write(pregunta)
            cosa.write(",")
            cosa.close()
            break

def nombre():
    while True:
        cosa = open("lote.csv","a+")
        nom = input("Ingrese su nombre: ")
        if re.match("^.{5,30}$", nom):
            cosa.write(nom)
            cosa.write(",")
            cosa.close()
            break
        elif nom == "":
            print("no se puede dejar este caracter vacio")
        
def unidades():
    while True :
        cosa = open("lote.csv","a+")
        numero = int(input("Ingrese un valor ,asegurese que sea mayor o igual de 100\n y menor o igual de 1000: "))
        if numero <100 or numero >1000:
            print("numero no acceptable ")
            continue
        elif numero>=100 and numero<=1000:
            numero = str(numero)
            cosa.write(numero)
            cosa.write("\n")
            cosa.close()
            
            break

def menu():
    i= 0
    while i < 4 :
        if i == 0:
            print(clave())
            i += 1
        elif i == 1:
            print(nombre())
            i += 1
        elif i == 2 :
            print(getCaducidad())
            i += 1
        elif i == 3 :
            print(unidades())
            x = input("Desea agregar otro dato? S/N = ")
            x.upper
            if x == "S":
                i = 0
            elif x == "N":
                print("Adios")
                break
    
print(menu())
        
