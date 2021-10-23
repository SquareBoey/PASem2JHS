"""sita para datos
reclamo = [14, 9, 16, 9,16]
compara = 0
contador = 0
extra = 0
i = 0
while i < 5:
    if i <= 3:
        if reclamo[i] == reclamo[i+1]:
            compara = reclamo[i] 
            contador = contador + 1
        else:
            continue
    else:
        if reclamo[i-1] == reclamo[i]:
            if compara == reclamo[i]:
                contador = contador+1
            else:
                continue
        else:
            continue  
    i = i + 1

print("hola ",compara ,"hola ",contador )"""


#creamos la lista para los reclamos
reclamos = [14, 9, 16, 9,16]
print (reclamos) 
#hacemos el procedimiento de media 
media = sum(reclamos)/len(reclamos)
print ("media= ",media)


# moda 
# #
# el primer procedimiento para verificar que numero se repute 
repetido = 0 
modas = []
for i in reclamos: 
    aparicion = reclamos.count(i) 
    if aparicion > repetido: 
        repetido = aparicion 
        for i in reclamos:
            aparicion = reclamos.count(i) 
            if aparicion == repetido and i not in modas:
                modas.append(i)
                print ("moda:", modas) 
               
# mediana 

reclamos.sort() 
print (reclamos)
mediana =reclamos[2]
print ('mediana:',mediana)