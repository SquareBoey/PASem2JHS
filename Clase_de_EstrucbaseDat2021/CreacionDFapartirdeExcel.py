#Creacion de un dataframe a partor de un fichero .csv o Documento EXCEL
import pandas as pd 
# Importación del fichero datos-colesteroles.csv
df = pd.read_csv('https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesteroles.csv', sep=';', decimal=',')
print(df.head())