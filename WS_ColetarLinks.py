import requests
import re
import pandas as pd
import openpyxl
from bs4 import BeautifulSoup

urls = ['https://csgostash.com/stickers/regular','https://csgostash.com/stickers/tournament']

pages = []

for url in urls:
    response = requests.get(url)
    content = response.content
    site = BeautifulSoup(content, 'html.parser')

    # Contar paginação

    page_count = site.find('div', attrs = {'class' : 'col-lg-12 col-widen pagination-nomargin'})
    vet_count = [page_count.text]

    count = re.findall("[0-9]+", str(vet_count))
    quantidade_paginas = count[-1]
    quantidade_paginas = int(quantidade_paginas)
    print('Quantidade de páginas = ' + str(quantidade_paginas))

    # Lista de páginas

    for i in range(quantidade_paginas):
        count = int(i + 1)
        count = str(count)
        text = str('?page=')

        next_page = url + text + count
        count = int(count)
        pages.append([next_page])

    # Salvar links em um arquivo

    url_list = []

    for page in pages:
        url = (list(page))
        url_list.append([url])
        #print(url)

df_url = pd.DataFrame(url_list, columns = ['link'])
df_url.to_excel('url_list.xlsx', index = False)