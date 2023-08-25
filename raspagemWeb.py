import requests
import pandas as pd

texto_string = requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html').text
print(texto_string[:100])

print('\n----------------------------------------------------------------------------------------------------')

from bs4 import BeautifulSoup

bsp_texto = BeautifulSoup(texto_string, 'html.parser')
lista_noticias = bsp_texto.find_all('span', attrs={'class':'short-desc'})

print(type(bsp_texto))
print('\n----------------------------------------------------------------------------------------------------')
print(type(lista_noticias))
print('\n----------------------------------------------------------------------------------------------------')
print(lista_noticias[5])
print('\n----------------------------------------------------------------------------------------------------')
print(lista_noticias[5].contents)

print('\n----------------------------------------------------------------------------------------------------')
dados = []

for noticia in lista_noticias:
    data = noticia.contents[0].text.strip() + ', 2017' # Dessa informação <strong>Jan. 25 </strong> vai extrair Jan. 25, 2017
    comentario = noticia.contents[1].strip().replace("“", '').replace("”", '')
    explicacao = noticia.contents[2].text.strip().replace("(", '').replace(")", '')
    url = noticia.find('a')['href']
    dados.append((data, comentario, explicacao, url))

print(dados[1])

print('\n----------------------------------------------------------------------------------------------------')


df_noticias = pd.DataFrame(dados, columns=['data', 'comentário', 'explicação', 'url'])

print(df_noticias.shape)
print(df_noticias.dtypes)
print(df_noticias.head())

