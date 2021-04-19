fruta = []
i = 0
while i <5 :
    fruta.append(int(input("ingrese 5 valores")))
    i += 1
multiplicado = fruta.copy()

s = 0 
while s < i:
    multiplicado[s] = multiplicado[s] * 2
    s += 1

print(fruta)
print(multiplicado)