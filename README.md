# The Oscars

This app let you check information regarding any actress, actor, director that has been nominated in any Oscar ceremony since 1927.

## Background

My app is based in the dataset ´The Oscar Award, 1927 - 2018´ from kaggle (https://www.kaggle.com/unanimad/the-oscar-award). 
I've cleaned name and film columns to get rid of special charactes and I've created a new column `cat__c` that includes a shorter list of current categories from column `category`.

The information shown is supplemented by information scrapped from IMDB and Wikipedia. 

## Directories and Files

- `src` contains the app (`main.py`) and several python files that include the different functions used in the pipeline.
- `input` contains source files for some of the functions as well as the initial dataset.
- `output`is divided in three different directories that collect that collect the outputs depending on the way the user uses to get the information.

## Getting Started

There are three ways that you have in order to get information.

1. Using `Name + [actor|actress|director]` parameters: This command will show you information regarging the person:
    - Name
    - Birth date
    - Birth place 
    - Total movies
    - Oscars nomination information
    - It will generate into output/name directory:
        - A graph that shows on a timeline the amount of movies in which she or he have taken part. 
        - A list of all movies (csv)
2. Using `option --movie='NameOfMovie'`. You'll get:
    - Information regarding the nominated categories.
    - Synopsis
    - Director
    - Budget, Opening Weekend USA, Gross USA, umulative Worldwide Gross
    - It will generate into output/movie directory:
        - A pdf with the Oscars information
3. Using `option --year=year` You'll get:
    - It will print list of all nomitations
    - It will generate a pdf containig this information as well as a csv

### Prerequisites

You will need to install the following modules:

- `argparse`
- `pandas as pd`
- `requests`
- `BeautifulSoup from bs4`
- `re`
- `numpy as np`
- `matplotlib.pyplot as plt`
- `seaborn as sns`
- `tabulate from tabulate`
- `pdfkit as pdf`


Hope you enjoy it! :) 








