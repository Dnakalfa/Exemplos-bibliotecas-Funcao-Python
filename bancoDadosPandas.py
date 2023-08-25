import pandas as pd

df_etanol = pd.read_csv('etanol.csv', sep=';', encoding="ISO-8859-1")

print(df_etanol.info())
print(df_etanol.head(2))

df_etanol.drop(columns=['PRODUTO','MOVIMENTO COMERCIAL','UNIDADE'], inplace=True)

print(df_etanol.head(5))

df_etanol.set_index(keys='ano', drop=True, inplace=True)

print(df_etanol.head(2))

