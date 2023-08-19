import requests
import re
import pandas as pd
import openpyxl
from bs4 import BeautifulSoup

# Importar arquivo
'''
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
''' 
0:14 - Stickers Regulares
15:  - Stickers de torneio
'''
'''
stk_regulars = sticker[0:14]
stk_tournaments = sticker[15:]
'''
# Loop para percorrer os links dos stickers regulares
'''
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
        link = str(sticker.find('a'))
        padrao = re.compile('<(.*?)>')
        achado = padrao.match(str(link))
        link = achado.group(1)
        link = link[8:-1]

        name = sticker.find('div', attrs={'class': 'well result-box nomargin'})
        name = name.find('h3')
        name = name.text
        name = name.replace('\n', '')

        price = sticker.find('div', attrs={'class': 'price'})
        price = price.text
        price = price[4:]
        price = price.replace('.', '').replace(',', '.')
        price = price.replace('\n', '')

        listings = sticker.find('a', attrs={'class': 'btn btn-default market-button-item'})
        listings = listings.text
        listings = re.sub('[^0-9]', '', listings)
        listings = listings.replace('\n', '')

        # Acessa o link do sticker e coleta volume

        url = link
        response = requests.get(url)
        content = response.content
        site = BeautifulSoup(content, 'html.parser')

        volume = site.select('td')[2]
        volume = volume.text
        volume = re.sub('[^0-9]', '', volume)
        volume = volume.replace('\n', '')

        sticker_list.append([name, price, listings, volume])

#print(sticker_list)

# Colocar em um dataframe e salvar em arquivo

df_regular_sticker = pd.DataFrame(sticker_list, columns = ['name', 'price', 'listings', 'volume'])
df_regular_sticker.to_excel('data_regular_stickers.xlsx', index = False)
'''
# Loop para percorrer os links dos stickers de torneio
stk_tournaments = [
    "https://csgostash.com/stickers/tournament/Paris+2023?page=1",
    "https://csgostash.com/stickers/tournament/Paris+2023?page=2",
    "https://csgostash.com/stickers/tournament/Paris+2023?page=3",
    "https://csgostash.com/stickers/tournament/Paris+2023?page=4",
    "https://csgostash.com/stickers/tournament/Paris+2023?page=5",
    "https://csgostash.com/stickers/tournament/Paris+2023?page=6",
    "https://csgostash.com/stickers/tournament/Paris+2023?page=7",
    "https://csgostash.com/stickers/tournament/Paris+2023?page=8",
    "https://csgostash.com/stickers/tournament/Paris+2023?page=9",
    "https://csgostash.com/stickers/tournament/Paris+2023?page=10",
    "https://csgostash.com/stickers/tournament/Paris+2023?page=11",
    "https://csgostash.com/stickers/tournament/Paris+2023?page=12"
]
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
        link = str(sticker.find('a'))
        padrao = re.compile('<(.*?)>')
        achado = padrao.match(str(link))
        link = achado.group(1)
        link = link[8:-1]

        #tournament = sticker.find('h4')
        #tournament = tournament.text
        #tournament = tournament.replace('\n', '')

        url = link
        response = requests.get(url)
        content = response.content
        site = BeautifulSoup(content, 'html.parser')

        name = site.find('div', attrs={'class': 'row text-center'})
        name = name.find('h2')
        name = name.text
        name = name.replace('\n', '')

        imageurl = site.find('img', attrs={'class': 'img-responsive center-block item-details-img'})
        imageurl = str(imageurl)
        imageurl = re.search("(?P<url>https?://[^\s]+)", imageurl).group("url")
        imageurl = imageurl[:-3]

        #price = site.find('div', attrs={'class': 'col-md-6 col-md-6-collapse-top-margin'})
        #price = price.find('span', attrs={'class': 'pull-right'})
        #price = price.text
        #price = price[3:]
        #price = price.replace('.', '').replace(',', '.')
        #price = price.replace('\n', '')
        #price = price.replace('Recent Price', '')

        #listings = site.select('td')[0]
        #listings = listings.text
        #listings = re.sub('[^0-9]', '', listings)
        #listings = listings.replace('\n', '')

        #volume = site.select('td')[2]
        #volume = volume.text
        #volume = re.sub('[^0-9]', '', volume)
        #volume = volume.replace('\n', '')

        sticker_list.append([name, imageurl])

#print(sticker_list)

# Colocar em um dataframe e salvar em arquivo

df_tournament_sticker = pd.DataFrame(sticker_list, columns = ['name', 'imageurl'])
df_tournament_sticker.to_excel('data_tournament_stickers.xlsx', index = False)
