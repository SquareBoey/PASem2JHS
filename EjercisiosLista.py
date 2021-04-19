lista = []

num = int(input("Desde que numero"))

for i in range(1,num + 1):
    lista.append(i)

lista.reverse()

for i in range(len(lista)):
    print(lista[i])