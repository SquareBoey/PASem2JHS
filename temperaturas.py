#primero pongo los datos que voy a utilizar y no quiero que se rinicien dentro del ciclo
tempdia = [] 
dias =int(input("cuantos dias se van a medir? "))
cont = 0
suma = 0 
while cont < dias:
    #dentro del ciclo puedo añadir los datos ingresados del usuari
    # o dentro de suma y al mismo timepo añadirlos a la lista
    i = int(input("Temperatura del dia = "))
    suma = suma + i 
    #usamos el .append para agruegar todos los datos del usuario al final de la lista a como los escriban
    tempdia.append(i)
    #este contador es para salir del ciclo while 
    cont = cont + 1
#El comando sort lo utilise para acomodar los numeros de menor a mayor
tempdia.sort()
#a la variable sancho fue creada para obtener la cantidad de numeros 
# ingresados por el usuario y asi resolverlo dentro del print
sancho = len(tempdia)
print("La temperatura minima fue ",min(tempdia),max(tempdia))
print("su promedio es ",suma  / sancho)