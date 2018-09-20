import pandas as pd

pd.core.common.is_list_like = pd.api.types.is_list_like

import pandas_datareader.data as web

df=web.DataReader('USD000UTSTOM', 'moex', start='2010-07-01', end='2017-07-31')

print(df.head())
print(df.tail())
print(df.describe())
print(df.info())






    
