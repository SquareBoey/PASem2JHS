def menu():
    alberca = 0 
    alberca = int(input("Opciones: \n1)Binario \n2)Octal \n3)Decimal \n4)Hexadecimal \nEliga el sistema del cual desea traducir: "))
    if alberca == 1:
        print("mesa que mas aplauda")
    elif alberca == 2:
        print("Huele a obo")
    elif alberca == 3:
        print(decimal())
 

def decimal():
    opcion = int(input("A que lenguaje desea traducir \n1)binario \n2)Hexadecimal \n3)Octal \nIntraduzca su respuesta = "))
    pedro = []   
    """opcion uno es de decimal a binario 
    tengo un chingo de cosas por hacer """
    ciclo = 0 
    if opcion == 1 :   
        elnumero = int(input("Ingrese el numero que desea cambiar a binario = "))
        contenedor = elnumero
        while ciclo < 1:
            primerbin = int(contenedor % 2 )
            dividio = int(contenedor / 2)
            pedro.append(primerbin)
            contenedor = dividio
            if contenedor < 1 :
                ciclo +=1
        pedro.reverse()
        print("su numero en Binario es = ",pedro)
    #Bueno ya con este quedaron dos numeros de decimal a otro lenguaje listo calisto
    elif opcion == 2:
        acum = ""
        num = int(input("ingrese el numero decimal para pasar a Hexadecimal = "))
        x = num
        while True:
            if x%16>9 and x%16<16:
                if x%16==10:
                    acum = "A"+acum
                if x%16==11:
                    acum = "B"+acum
                if x%16==12:
                    acum = "C"+acum
                if x%16==13:
                    acum = "D"+acum
                if x%16==14:
                    acum = "E"+acum
                if x%16==15:
                    acum = "F"+acum
            else:
                acum = str(x%16)+acum
            x = int(x/16)
            if x<=1: break
        if x>0:
            acum = str(x)+acum
        print(num," Decimal = ",acum," en Hexadecimal")
    elif opcion == 3:
        numero = int(input("numero de decimal a octal = "))
        print(numero," a El sistema octal es = ",oct(numero))

def binario():
    opcion = int(input("Seleccione a que lenguaje desea cambiar a \n 1)Decimal: "))
    if opcion == 1:
        #binario a decimal
        cuarzo = input("ingrese el numero binario que desea transformar a decimal: ")
        x = len(cuarzo)
        i=0
        sum = 0
        while i < len(cuarzo):
            f = int(len(cuarzo))
            print(cuarzo[i])
            abso = int(cuarzo[i])
            f = f - i
            transfo = abso * (2 **f-1)
            sum = sum + transfo
            i += 1
        print(sum)
            


print(menu())