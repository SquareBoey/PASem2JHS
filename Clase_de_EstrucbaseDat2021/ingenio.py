from numpy import float64
import pandas as pd 
#creacion de serie a base de una lista 
joy = pd.Series([1,2,2,3,3,3,4,4,4,4],dtype = float64)
#se creo la serie a base de un diccionario
s = pd.Series({'Matemáticas': 6.0,  'Economía': 4.5, 'Programación': 8.5})
#Esta de aqui es de acceso por pocicion
print(s[1:3])
#Accesso por indice 
print(s['Economía'])
print(s[['Programación','Matemáticas']])
#atributos de una serie 
print(s.size)
print(s.index)
print(s.dtype)
