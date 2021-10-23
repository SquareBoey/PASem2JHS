import pandas as pd
#resumen descriptivo de una serie 
s = pd.Series([1, 1, 1, 1, 2, 2, 2, 3, 3, 4])
#funciones de panda que ayudan a resumir varios aspectos de una serie
print(s.count())
print(s.sum())
print(s.cumsum())
print(s.value_counts())
print(s.min())
print(s.max())
print(s.mean())
print(s.std())
print(s.describe())