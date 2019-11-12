import pandas as pd
import re

df = pd.read_csv('input/the_oscar_award.csv')

def CorrigeCaracteresRaros(df,lista_columnas):
    '''
    Corrige los caracteres raros de la codificacióni cp1255 y devuelve
    el texto de las columnas que queramos correctamente
    '''
    for col in lista_columnas:
        df[col] = df[col].apply(lambda x: x.encode('cp1252').decode('utf-8'))

CorrigeCaracteresRaros(df, ['name','film'])

def cat(e):
    l = ['ACTOR','ACTRESS','WRITING','MUSIC','SHORT SUBJECT','SPECIAL ACHIEVEMENT AWARD','SHORT FILM','CINEMATOGRAPHY','DIRECTING','ART DIRECTION','COSTUME DESIGN','DOCUMENTARY']
    for i in l:
        result = re.search(i, str.upper(str(e)))
        if result:
            return i
    else:
        return e

df['cat__c'] = df['category'].apply(cat,1)

df.to_csv('df.csv', index = False)


