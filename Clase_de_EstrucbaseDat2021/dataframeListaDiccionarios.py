#creacion de DataFrames de una lista de ddiccionarios
import pandas as pd 
df = pd.DataFrame([{'Nombre':'María', 'Edad':18},
 {'Nombre':'Luis', 'Edad':22},
  {'Nombre':'Carmen'}])
print(df)