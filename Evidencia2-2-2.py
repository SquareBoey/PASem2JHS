numeros=[1,2,3,4,5,-5,-15,-25,-3,-4]

i = 0
sumapos = 0 
sumaneg = 0

while i <10:
    absorver = numeros[i]
    if absorver >= 0:
        sumapos = sumapos + absorver
    else:
        sumaneg = sumaneg + absorver
    i += 1

print("La suam de numeros positivos es ",sumapos,"la suma de numeros negativos es ",sumaneg)