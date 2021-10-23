#como hacer el filtrado de una serie
import pandas as pd
s = pd.Series({'Matemáticas': 6.0,  'Economía': 4.5, 'Programación': 8.5})
print(s[s > 5])