import seaborn as sns
import matplotlib.pyplot as plt

# Configurando o visual do gráfico. Leia mais em https://seaborn.pydata.org/generated/seaborn.set.html#seaborn.set
sns.set(style="darkgrid") # opções: darkgrid, whitegrid, dark, white, ticks

df_tips = sns.load_dataset('tips')


#Exemplo 1 de graficos barplot\estimator
#print(df_tips.info())
df_tips.head()

fig, ax = plt.subplots(1, 3, figsize=(15, 5))

sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[0])
sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[1], estimator=sum)
sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[2], estimator=len)


#Exemplo 2 de graficos
plt.figure(figsize=(10, 5))

ax = sns.barplot(x="day", y="total_bill", data=df_tips)

ax.axes.set_title("Venda média diária", fontsize=14)
ax.set_xlabel("Dia", fontsize=14)
ax.set_ylabel("Venda média ", fontsize=14)
ax.tick_params(labelsize=14)

#graficos 3 countplot

plt.figure(figsize=(10, 5))
sns.countplot(data=df_tips, x="day")

plt.figure(figsize=(10, 5))
sns.countplot(data=df_tips, x="day", hue="sex")

#graficos 4 scatterplot

plt.figure(figsize=(10, 5))
sns.scatterplot(data=df_tips, x="total_bill", y="tip")

