import pandas as pd 
s = pd.Series({'Matemáticas': 6.0,  'Economía': 4.5, 'Programación': 8.5})
print(s.sort_values())
print(s.sort_index(ascending = False))