import pandas as pd
from math import log
s = pd.Series([1, 2, 3, 4])
print(s.apply(log))