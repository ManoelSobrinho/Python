import requests
import re
import pandas as pd
import openpyxl
from bs4 import BeautifulSoup

# Definir URL a ser lido
url = "https://csgostash.com/stickers/tournament/Paris+2023"
#print(type(url))
response = requests.get(url)
#print(response.content)
content = response.content
site = BeautifulSoup(content, 'html.parser')
#print(site.prettify())

# Página com o conteúdo

stickers = site.findAll('div', attrs = {'class' : "col-lg-4 col-md-6 col-widen text-center"})
#print(stickers)

# Contar paginação

page_count = site.find('div', attrs = {'class' : 'col-lg-12 col-widen pagination-nomargin'})
vet_count = [page_count.text]

count = re.findall("[0-9]+", str(vet_count))
quantidade_paginas = count[-1]
quantidade_paginas = int(quantidade_paginas)
print('Quantidade de páginas = ' + str(quantidade_paginas))

# Lista de páginas

pages = []

for i in range(quantidade_paginas):
    count = int(i + 1)
    count = str(count)
    text = str('?page=')

    next_page = url + text + count
    count = int(count)
    pages.append([next_page])
    #print(next_page)

#print(pages)
#print(pages)

# Percorrer páginas

for page in pages:
    url = (str(page))
    print(url)
    #response = requests.get(url)
    #content = response.content
    #site = BeautifulSoup(content, 'html.parser')
    #sitkers = site.findAll('div', attrs = {'class' : "col-lg-4 col-md-6 col-widen text-center"})

# Leitura e tratamento dos dados

sticker_list = []

for sticker in stickers:
    link = str(sticker.find('a'))
    padrao = re.compile('<(.*?)>')
    achado = padrao.match(str(link))
    link = achado.group(1)
    link = link[8:-1]

    url = link
    response = requests.get(url)
    content = response.content
    site = BeautifulSoup(content, 'html.parser')
'''
    padrao = re.compile('<(.*?)>')
    achado = padrao.match(str(link))
    link = achado.group(1)
    link = link[8:-1]
'''
    name = sticker.find('div', attrs={'class': 'well result-box nomargin'})
    name = name.find('h3')
    name = name.text
    name = name.replace('\n', '')

    rarity = sticker.find('p', attrs={'class': 'nomargin'})
    rarity = rarity.text
    rarity = rarity.replace('\n', '')

    price = sticker.find('div', attrs={'class': 'price'})
    price = price.text
    price = price[4:]
    price = float(price.replace('.', '').replace(',', '.'))

    sticker_list.append([link, name, rarity, price])

print(sticker_list)
#print(type(sticker_list))

# Colocar em um dataframe e salvar em arquivo

#df_sticker = pd.DataFrame(sticker_list, columns = ['link', 'name', 'rarity', 'price'])
#df_sticker.to_excel('stickers.xlsx', index = False)

#print(df_sticker)