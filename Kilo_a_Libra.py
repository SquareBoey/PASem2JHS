opcion = ""

while True:
    opcion = input("Elija una de las sigiuientes opciones\n A) De kilos a Libras B) De Libras a Kilos")
    opcion = opcion.upper()
    if opcion == "A" or opcion == "B":
        break




if opcion == "A":
    kilos = float(input("Ingrese el peso en kilos de su item: "))
    Libras = kilos / 0.454
    print("El peso de su objeto en libras seria ",Libras," Libras")
elif opcion == "B":
    Libras = float(input("Ingrese el peso de su objeto en Libras: "))
    kilos= Libras * .454
    print("El Peso de su item en kilos es de ",kilos,"Kg")