class Circulo():
    def __init__(self,radio,altura):
        self.radio = radio
        self.altura = altura
    
    def area(self):
        self.areaC = (3.1416*(self.radio*self.radio))
        return self.areaC

    def prisma(self):
        self.prismaC = (self.areaC * self.altura)
        return self.prismaC

    def piramide(self):
        self.volpir =((self.areaC * self.altura)/3)
        return self.volpir

class Rectangulo():
    def __init__(self,base_r,altura_r,altura):
        self.base_r = base_r
        self.altura_r = altura_r
        self.altura = altura
    
    def area(self):
        self.arear = (self.base_r * self.altura_r)
        return self.arear

    def prisma(self):
        self.areaP =(self.arear * self.altura)
        return self.areaP

    def piramide(self):
        self.areapiramide = ((self.arear * self.altura) / 3)
        return self.areapiramide

class Triangulo():
    def __init__(self,base_t,altura_t,altura):
        self.base_t = base_t
        self.altura_t = altura_t
        self.altura = altura

    def area(self):
        self.areat = ((self.base_t * self.altura_t)/2)
        return self.areat

    def prisma(self):
        self.areprisma = (self.areat * self.altura)
        return self.areprisma
    
    def piramide(self):
        self.arepira = ((self.areat * self.altura)/3)
        return self.arepira 



def menu2():
    opti = 0
    while opti == 0:
        wena = int(input("Que proceso desea realisar? \n1.-Circulo/prisma circular \n2.-Rectangulo/prisma rectangular \n3.-Triangulo/prisma triangular \n4.-Salir \nSeleccione una opcion: "))
        if wena == 1:
            alfredo = Circulo(float(input("ingresa valor de radio")),float(input("ingresa valor de altura")))
            print("El area de tu circulo es ",alfredo.area())
            print("El volumen de tu prisma es ",alfredo.prisma())
            print("El volumen de tu piramide es",alfredo.piramide())
        elif wena == 2:
            juanjo = Rectangulo(float(input("ingresa valor de base del rectangulo ")),float(input("ingresa valor de la altura del rectangulo ")),float(input("ingresa valor de la altura del prisma/piramide")))
            print("el area de el rectangulo es ", juanjo.area())
            print("el area de tu prisma rectangular es ",juanjo.prisma())
            print("el area de tu piramide rectangular es ",juanjo.piramide())
        elif wena == 3:
            hector = Triangulo(float(input("ingresa valor de base del triangulo ")),float(input("ingresa valor de la altura del triangulo ")),float(input("ingresa valor de la altura del prisma/piramide ")))
            print("el area de el rectangulo es ", hector.area())
            print("el area de tu prisma rectangular es ",hector.prisma())
            print("el area de tu piramide rectangular es ",hector.piramide())
        else:
            print("se cierra el programa")
            opti = opti + 1 

print(menu2())