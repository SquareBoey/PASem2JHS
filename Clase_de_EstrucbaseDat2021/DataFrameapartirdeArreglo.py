#Creacion de dataframe a partir de un array
import pandas as pd 
import numpy as np
df = pd.DataFrame(np.random.randn(4, 3), columns=['a', 'b', 'c'])
print(df)