def llenarLista(l):
    for i in range(2, 100):
        div = 0
        for j in range(1, i + 1):
            if i % j == 0:
                div += 1
        if div == 2:
            l.append(i)

lista = []
llenarLista(lista)
for i in range(len(lista)):
    print(lista[i])