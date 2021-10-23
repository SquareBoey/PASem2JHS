import csv,re,os

nombre = ""
#esto verifica que el archivo exista 
if os.path.exists("micasita.csv"):
    archivo = open("micasita.csv",'r')
    archivo.write("CORREO|NOMBRE|NACIMIENTO")
    archivo.close
else:
    open("micasita.csv","w")
