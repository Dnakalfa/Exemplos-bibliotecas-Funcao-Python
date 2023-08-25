import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 


df_satelites = pd.read_csv('satelites_operando_comercialmente.csv', sep=';') 
df_satelites.drop_duplicates(inplace=True)
df_satelites.reset_index(drop=True, inplace=True)

#print(df_satelites.info())
print(df_satelites.head())

# Quantos satélites são brasileiros e quantos são estrangeiro?
plt.figure(figsize=(5,3))
plt.tick_params(labelsize=12)
sns.countplot(data=df_satelites, x='Tipo de Direito')

# quantos satétiles cada operadora brasileira possui operando?
df_satelites_brasileiros = df_satelites.loc[df_satelites['Tipo de Direito'] == 'Brasileiro']

plt.figure(figsize=(15,5))
plt.xticks(rotation=90)
plt.tick_params(labelsize=12)
sns.countplot(data=df_satelites_brasileiros, x='Operadora comercial')

# Quantos satélites brasileiros estão operando em cada banda?

plt.figure(figsize=(15,5))
plt.xticks(rotation=90)
plt.tick_params(labelsize=12)
sns.countplot(data=df_satelites_brasileiros, x='Bandas do satélite')

# Quantos satétiles cada operadora estrangeira possui operando?

df_satelites_estrangeiros = df_satelites.loc[df_satelites['Tipo de Direito'] == 'Estrangeiro']

plt.figure(figsize=(15,5))
plt.xticks(rotation=90)
plt.tick_params(labelsize=12)
sns.countplot(data=df_satelites_estrangeiros, x='Operadora comercial')

# Quantos satélites brasileiros estão operando em cada banda?

plt.figure(figsize=(15,5))
plt.xticks(rotation=90)
plt.tick_params(labelsize=12)
sns.countplot(data=df_satelites_estrangeiros, x='Bandas do satélite')