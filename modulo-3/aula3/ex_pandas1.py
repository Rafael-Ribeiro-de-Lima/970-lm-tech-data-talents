import pandas as pd
import numpy as np

df = pd.DataFrame({'Nomes':['Tom', 'Ron', 'Leslie', 'Jerry'],
                   'Nota':[10,7,10,2],
                   'Passou':['sim','sim','sim','não']})

print(df.head())

df.dropna(axis=0, inplace=True)

print(df.groupby('Passou')['Nota'].sum())

