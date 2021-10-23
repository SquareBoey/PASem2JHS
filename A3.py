import re,datetime

def getCaducidad():
        while True:
            try:
                caducidad = input("Fecha de caducidad (aaaa-mm-dd): ")
                if (caducidad ==""):
                    print("La fecha de caducidad no se puede omitir.")
                else:
                    if (re.match(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", caducidad)):
                        print("La caducidad es de: ")
                        anio=int(caducidad[0:4])
                        mes=int(caducidad[5:7])
                        dia=int(caducidad[-2:])
                        caducidad = datetime.date(anio, mes, dia)
                        return caducidad
                    else:
                        print("El dato no está en formato aaaa-mm-dd.")
            except ValueError:
                print("La fecha no es una fecha válida.")

print(getCaducidad())