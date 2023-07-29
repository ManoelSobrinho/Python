import requests
import re
import pandas as pd
import openpyxl
from bs4 import BeautifulSoup

# Importar arquivo

df_stickers = pd.read_excel("url_list.xlsx")

# Transformar DataFrame em Lista

sticker = df_stickers.values.tolist()

# Eliminar caracteres da lista:
    # [
    # ]
    # '

eliminar = ['[',']','\'']

trans = {ord(i): '' for i in eliminar}
sticker = [j.translate(trans) for i in sticker for j in i]
#print(sticker)

# Separando stickers regulares de torneio

''' 
0:14 - Stickers Regulares
15:  - Stickers de torneio
'''

stk_regulars = sticker[0:14]
stk_tournaments = sticker[15:]

# Loop para percorrer os links dos stickers regulares

sticker_list = []

for stk in stk_regulars:

    # Definir URL a ser lido

    url = stk
    #print(type(url))
    response = requests.get(url)
    #print(response.content)
    content = response.content
    site = BeautifulSoup(content, 'html.parser')
    #print(site.prettify())

    # Página com o conteúdo

    stickers = site.findAll('div', attrs = {'class' : "col-lg-4 col-md-6 col-widen text-center"})

    # Leitura e tratamento dos dados

    for sticker in stickers:
        name = sticker.find('div', attrs={'class': 'well result-box nomargin'})
        name = name.find('h3')
        name = name.text
        name = name.replace('\n', '')

        sticker_list.append(name)

print(sticker_list)

# Loop para percorrer os links dos stickers regulares

sticker_list = []

for stk in stk_tournaments:

    # Definir URL a ser lido

    url = stk
    #print(type(url))
    response = requests.get(url)
    #print(response.content)
    content = response.content
    site = BeautifulSoup(content, 'html.parser')
    #print(site.prettify())

    # Página com o conteúdo

    stickers = site.findAll('div', attrs = {'class' : "col-lg-4 col-md-6 col-widen text-center"})

    # Leitura e tratamento dos dados

    for sticker in stickers:
        name = sticker.find('div', attrs={'class': 'well result-box nomargin'})
        name = name.find('h3')
        name = name.text
        name = name.replace('\n', '')

        tournament

        capsule

        sticker_list.append(name, tournament, capsule)

print(sticker_list)




