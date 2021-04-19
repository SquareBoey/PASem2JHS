milista = []
i = 0
NumMax = int()
NumMin = int()
numpacont = 0

while i < 10 :
    milista.append(int(input("Ingrese el valor de la lista numero" )))
    x = milista[i]
    if i == 0:
        NumMin = x 
        NumMax = x
    if x % 2 == 0:
        numpacont += 1
    if x > NumMax:
        NumMax = x 
    if x < NumMin:
        NumMin = x
    i += 1
        
print("La cantidad de numeros par es ",numpacont," El numero maximo es ",NumMax," El numero minimo es ",NumMin)
