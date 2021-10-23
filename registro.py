import os,re,csv
from Clases import participantes
#Ahora la lista personas son globales
personas = []

#variables que se agarraron gracias a programas de referencia distribuidos por profesor#
LimpiarPantalla = lambda: os.system('cls')
rutaarchivo = os.path.abspath(os.getcwd())



def RegEx(_txt,_regex): 
    coincidencia=re.match(_regex, _txt)
    return bool(coincidencia)

def main():#JHSV
    Menu()



def Menu():#Modificado por Jose Horacio SV
    while (True):
        LimpiarPantalla()
        print("LISTA DE COTACTOS")
        print(" ")
        print("[1] Cargar información de CSV")
        print("[2] Registrar participantes")
        print("[3] Buscar participante")
        print("[4] Modificar participante")
        print("[5] Eliminar participante ")
        print("[6] Ver Lista de participantes")
        print("[7] Actualizar informacion de CSV")
        print("[8] Serialisar informacion a JSON")
        print("[X] Salir")
        opcion_elegida = input("¿Qué deseas hacer?  > ")
        if RegEx(opcion_elegida,"^[123456780X]{1}$"):
            if opcion_elegida=="X":
                print("GRACIAS POR UTILIZAR EL PROGRAMA")
                break
            if opcion_elegida=="1":
                print(Cinfousu())
            if opcion_elegida=="2":
                print(registrar())
            if opcion_elegida=="3":
                print("Llamar procedimiento para la acción")
            if opcion_elegida=="4":
                print("Llamar procedimiento para la acción")
            if opcion_elegida=="5":
                print("Llamar procedimiento para la acción")
            if opcion_elegida=="6":
                print("Llamar a la funcion deseada ")
            if opcion_elegida=="7":
                print("Llamar a la funcion deseada ")
            if opcion_elegida=="8":
                print("Llamar a la funcion deseada ")

            input("Pulsa enter para contunuar...")
        else:
            print("Esa respuesta no es válida.")
            input("Pulsa enter para contunuar...")


#Jose Horacio
def Cinfousu():
    #primero informamos al usuario que se verificara si es la primera vez que se utiliza
     
    print("Bienvenido a Cargar informacion de usuario\n \n ")
    input("oprima enter para continuar>>>> ")
    if os.path.exists("micasita.csv"):
        with open("micasita.csv",newline="") as archivo_csv:
            lector_csv = csv.reader(archivo_csv, delimiter='|')
            for e in lector_csv:
               personas.append(participantes(e[0],e[1],e[2]))
    else:
         archivo = open("micasita.csv","w")
         archivo.write("CORREO|NOMBRE|NACIMIENTO")
         archivo.close()
    for o in personas:
         print(o.correo)
         print(o.nombre)
         print(o.nacimiento)

#Elabiorado Jose Horacio
def registrar():
    print("Bienvenido a registro de participantes \n \n ")
    while True:
        Correo = input("Ingrese un correo electronico valido>>> ")
        if Correo == "":
            break
        if re.match("^\w+[@]{1}\w+(\.com)$",Correo):
            print("el resto de este programa no puede ser utilizado")
            break
            """else:
                personas.append(Correo)
                nombre = input("Ingrese su nombre>>> ")
                personas.append(nombre)
                while True:
                    fechnac = input("ingrese una fecha de nacimiento en el formato YYYY/MM/DD\n >>>>>>> ")
                    if re.match(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$",fechnac):
                        personas.append(fechnac)
                        break
                    else:
                        print("Formato no valido \n \n ")"""
                
print(main())
