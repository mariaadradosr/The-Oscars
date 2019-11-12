import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def urlImdb(string):
    '''
    Se le pasa un string con un título o una persona y te devuelve
    la página principal de IMDB para ese título o persona
    '''
    result = ''
    for i in string.split(' '):
        result += ('+'+i)
    url= 'https://www.imdb.com/find?ref_=nv_sr_fn&q={}&s=all'.format(result.strip('+'))
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    return 'https://www.imdb.com'+ soup.find("table").find_all('tr')[0]('a')[1]['href']

def createSoup(url):
    return BeautifulSoup(requests.get(url).text, features="lxml")

def numPeliculas(soup, tipo):
    num = soup.find('div', {'id':'filmography'}).find('div', {'id':"filmo-head-{}".format(tipo)}).text.strip().split(' ')[1].replace('(', '')
    return 'Total movies as {} --> {}'.format(tipo, str(num))

def dfFilmografia(soup,tipo):
    movies = {'year':[], 'film':[]}
    for d in soup.find_all(id=re.compile('^{}-.*'.format(tipo))):
        movies['year'].append(d.find(class_='year_column').get_text(' ', strip=True).strip('/I')[:4])
        movies['film'].append(d.b.get_text(' ', strip=True))
    films = pd.DataFrame(movies)
    films['year'] = pd.to_numeric(films['year'], errors='coerce')
    films_ = films[films['year'].notnull()]
    films_['year'] = films_['year'].astype('int')
    films_.to_csv('../output/name/historico_peliculas.csv', index=False)
    return films_

def chartFilmografia(df):
    ev = df[(df['year'] != '') & (df['year'].notnull())].groupby('year', as_index = True).agg('count')
    ev.fillna(0)
    ev.index = ev.index.map(int)
    ev = ev.reindex(range(int(ev.index.min()), int(ev.index.max()+1)))
    plt.figure(figsize=(10, 5))
    sns.barplot(ev.index, ev['film'], palette = 'viridis')
    plt.xticks(rotation=60)
    ax = plt.axes()
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(True)
    ax.spines['left'].set_visible(True)
    plt.savefig('../output/name/filmografia.png', dpi= 100)


def infoPelicula(soupPeli):
    print('Sinopsis: ',soupPeli.find('div', {'class':"summary_text"}).text.strip(),'\n')
    print(soupPeli.find('div', {'class':"credit_summary_item"}).text.strip().replace('\n', ' '),'\n')
    print('Genre: ',str(soupPeli.select('#titleStoryLine > div:nth-child(10) > a')).split(' ')[2].replace('</a>',''))
    print('\n')
    for i in soupPeli.find_all('div', {'class':'txt-block'}):
        if re.search(r'Gross',i.text) or re.search(r'Opening',i.text) :
            print(i.text.replace('(estimated)','').replace('\n',''),'\n')
        if re.search(r'Budget',i.text.strip()):
            print(i.text.replace('(estimated)','').strip().replace('\n',''),'\n')

