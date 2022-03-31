import pandas as pd 
#creando un DataFrame a base de una lista de listas 
df = pd.DataFrame([['María', 18], ['Luis', 22], ['Carmen', 20]], 
columns=['Nombre', 'Edad'])
print(df)