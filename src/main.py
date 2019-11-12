#!/usr/bin/env python3 
import sys
import argparse
import subprocess
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import imdb
import data
from tabulate import tabulate
import pdfkit as pdf
import wiki

def recibeConfig():
    parser = argparse.ArgumentParser(description=''' 
    
    1) Print information regarding any actress, actor or director that 
    has been either nominated to or has won an Oscar since 1927 complete, typing name + category (eg. 'Uma Thurman' actress)
    
    2) Use --year in case you want to check nominees and winner of an specific year (eg, --year=1987)

    3) Use --movie if you wan't to check specific information regading a movie (eg, --movie='The Theory of Everything').
    ''')
    group = parser.add_argument_group('Consulta persona')
    group.add_argument('Name',
                        nargs = '?',
                        help='Name of the actor, actress or director',
                        #metavar='nombre',
                        type = str
                        # default=""
                        )
    group.add_argument('Category',
                        nargs = '?',
                        help='director | actor | actress',
                        #metavar='categoria',
                        type = str
                        # default=""
                        )
    parser.add_argument('--year',
                        nargs='?',
                        help='''Select a year to see the complete list of Oscar nominees and winners in categories
                                including Best Actress/Actor in leading role, Best Actress/Actor in a 
                                supporting role and Best Picture''',
                        #metavar='anyo',
                        type = int
                        # default=""
                        )
    parser.add_argument('--movie',
                        nargs='?',
                        help='''Select a movie to see the complete list of Oscar nominees and winners in categories
                                including Best Actress/Actor in leading role, Best Actress/Actor in a 
                                supporting role and Best Picture''',
                        #metavar='movie',
                        type = str
                        # default=""
                        )
                        
    args = parser.parse_args()
    print(args)
    return args



def main():
    # PASO 1 - Recibir flags y estandarizarlos en un dict
    config = recibeConfig()
    df = pd.read_csv('../input/df.csv')
    if config.year is None and config.movie is None:
        if len(df[(df['name'] == config.Name)]) > 0:
            print('\n')
            urlW = wiki.urlWiki(config.Name)
            soupW = imdb.createSoup(urlW)
            wiki.infoGeneral(soupW)
            print('\n')
            url = imdb.urlImdb(config.Name)
            soup = imdb.createSoup(url)
            print(imdb.numPeliculas(soup, config.Category))
            print('\n')
            print(data.resumenPremios(df, config.Name))
            print('\n')
            pdtabulate=lambda df:tabulate(df,headers='keys',tablefmt='psql')
            print(pdtabulate(data.tablaPremios(df, config.Name)))
            print('\n')
            print(" You'll find further information in /output/name")
            print('\n\n\n')
            dfFilm = imdb.dfFilmografia(soup,config.Category)
            imdb.chartFilmografia(dfFilm)
        else:
            print('\n\n{} has not been nominated yet :____(\n\nTRY ANOTHER NAME\n\n'.format(config.Name))
    
    if config.year is not None:
        if len(df[(df['year_ceremony'] == config.year)]) > 0:
            pd.set_option('display.max_rows', 500)
            pd.set_option('display.max_columns', 500)
            pd.set_option('display.width', 1000)
            # with pd.option_context('display.max_rows', None, 'display.max_columns', None):
            print(data.resumenYear(df, config.year))
            print('\n')
            print(" You'll find further information in /outpu/year")
            pdf.from_file('../input/resumenYear.html', '../output/year/resumenYear.pdf') 
        else:
            print('\n\n{} is out of range.\n\nPlase select a year from 1927 to 2019\n\n'.format(config.year))

    if config.movie is not None:
        if len(df[(df['film'] == config.movie)]) > 0:
            print('\n')
            print('The Oscars information:')
            print('\n')
            print(data.resumenPelicula(df, config.movie))
            print('\n')
            urlPeli = imdb.urlImdb(config.movie)
            soupPeli = imdb.createSoup(urlPeli)
            imdb.infoPelicula(soupPeli)
            print(" You'll find further information in /outpu/movie")
            print('\n')
            pdf.from_file('../input/resumenPelicula.html', '../output/movie/resumenPelicula.pdf') 
        else:
            print('\n\n{} is not among the nominated films.\n\nTRY ANOTHER FILM\n\n'.format(config.movie))

if __name__=="__main__":
    main()


