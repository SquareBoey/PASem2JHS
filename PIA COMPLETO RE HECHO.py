def nuevoemp():
    import datetime
    b = datetime.datetime.now()
    rep = 0
    while rep == 0:
        print("Menu de Nuevo empleado \n")
        archivo = open("textos.csv","a")
        nombre = input("Ingrese el nombre del empleado: ")
        Apepat = input("Apellido paterno: ")
        Apemat = input("Apellido materno: ")
        datebir =input("Fecha de nacimiento en formato dd/mm/aaaa: ")   
                        
        #Aqui convierto el paso de datebir en una lista 
        x = datebir.split("/")
        #en esta parte de abajo consigo lo que es el año actual que tenemos 
        FeActual = (b.strftime("%Y"))
        anocump = int(x[2])
        FeActual = int(FeActual)
        edad = FeActual - anocump
        print("Se ah capturado el nombre ",nombre," ",Apepat," ",Apemat,"Con una edad de ",edad," años")
                        
        #Aui lo que se hace es para poder anotar los datos en el documento que llamamos archivo 
        print("Desea ingresar otro empleado? ")
        wena = input("Quiere ingresar otro dato S o N: ")
        #Aqui es donde 
        if wena.lower() == "s":
            print(" ")
        #Aqui en esta parte intento cerrar el ciclo aunque de una manera poco optimisada , pero funciona 
        elif wena.lower() == "n":
            rep = rep + 1

def Ventas():
    bebed = 0
    while bebed == 0 :
        
        subtotal = 0
        while bebed == 0 :
            piezas = int(input("Cantidad de Piezas del Producto: ")) 
            if piezas ==0 : break  
            precio_unitario = float(input("Precio Unitario: ")) 
            importe = piezas * precio_unitario
            print(f"Importe: {importe}")
            subtotal = importe
            print(f"SubTotal: {subtotal}\n")
            IVA = subtotal * .16
            total = subtotal + IVA
            print(f"SubTotal: {subtotal}")
            print(f"IVA     : {IVA}")
            print(f"Total   : {total}")
            especial = input("Cliente cuenta con tarjeta especial? (S/N): ")
            if especial.lower() == "s":
                descuento = total * .05
                total = total - descuento
                print(f"Descuento  : {descuento}")
                print(f"Nuevo total: {total}")
            elif especial.lower() == 'n':
                desc=0
                total = total - desc
                print(f"Su descuento es de: {desc}")
                print(f"Nuevo total: {total}")
            pago = float(input("Su pago: "))   
                
            if pago >= total:
                print(f"Cambio: {pago-total}")
            else:
                print("ERROR en pago... insuficiente")
                        
            opti = input("Desea ingresar otra vez S/N")
                
            if opti.lower() == 's':
                print(" ")
            elif opti.lower() == 'n':
                bebed = bebed + 1
        

def calnom():
    finco = 0
    while finco == 0:
        print("Menu de pago de Trabajador")
        nombre = input("Cual es el nombre del empleado ")
        salario = float(input("Cuanto gana por hora "))
        horas = float(input("Cuantas horas laboro "))
        horarionormal = 40
        #Mientras horas se mayor horarionormal se realizara el sig procedimiento
        if horas > horarionormal:
            #Se calculan las horas extras
            horasextra = horas - horarionormal
            horanorm = horas
            #Se calculan las horas extras
            impuesto = .08
            #se calcula las horas sin horas extras
            horastopag = horas - horasextra
            horapag = horastopag * salario
            #Se calcula el pago por hora extra
            horaspag = horasextra * salario
            horasdoble = horaspag * 2
            #Se calcula el pago de nomina menos el impuesto
            horastotalpag = horapag + horasdoble
            salarioimpu= horastotalpag * impuesto
            print('Se retienen ', salarioimpu,'de impuestos')
            print("Trabajo ",horasextra,"horas extra")
            salariototal = horastotalpag - salarioimpu
            print('La nómina total del empleado es de: $',salariototal, 'pesos')
        else: 
            impuesto = .08
            horaA = horas * salario
            Salariob= horaA * impuesto
            print("Trabajo ",horasextra,"horas extra")
            print('Se retienen: $',Salariob,'de impuestos')
            nominatotal = horaA - Salariob
            print('La nómina total es de: $',nominatotal,'pesos')
                        
        cyc = input("Quiere hacer la cuenta de otro empleado? S/N")
                     
        if cyc.lower() == "s":
            print(" ")
        elif cyc.lower() == "n":
            finco = finco + 1
            

def menu():
    opti = 0
    while opti == 0:
        wena = int(input("Menu de opciones \n1)Registro de nuevo empleado \n2)Registro de venta \n3)Calculo de nomina \n4)Salir\nSeleccione una opcion: "))
        if wena == 1:
            nuevoemp()
        elif wena == 2:
            Ventas()
        elif wena == 3:
            calnom()
        else:
            print("se cierra el programa")
            opti = opti + 1 


print(menu())
print("Se ha cerrado el programa correctamente")