def resumenPremios(y, consulta):
    nominaciones = str(len(y[(y['name']==consulta)]))
    premios = str(len(y[(y['name']==consulta) & (y['win']==True)]))
    share = str(int(premios)/int(nominaciones)*100)[:4]
    return '{} has won {} Oscars out of {} nominations - {}%'.format(consulta, premios, nominaciones, share)


def tablaPremios(y, consulta):
     return y[['film','win','category','year_ceremony']][(y['name']==consulta)].groupby(['year_ceremony','category','film','win']).agg('count')


def resumenYear(y, year):
    # df_1 = y[(y['cat__c'] == 'ACTOR')|(y['cat__c'] == 'BEST PICTURE')|(y['cat__c'] == 'ACTRESS')|(y['cat__c'] == 'DIRECTING')]
    df_2 =  y[['film','win','category','year_ceremony','name']] [(y['year_ceremony'] == year) ]
    df = df_2.groupby(['year_ceremony','category','name','film','win']).agg('count')
    df.reset_index().to_csv('../output/year/resumenYear.csv', index=False)
    df.to_html('../input/resumenYear.html')
    return df.reset_index()

def resumenPelicula(y, pelicula):
    # df_1 = y[(y['cat__c'] == 'ACTOR')|(y['cat__c'] == 'BEST PICTURE')|(y['cat__c'] == 'ACTRESS')|(y['cat__c'] == 'DIRECTING')]
    df_2 =  y[['film','win','category','year_ceremony','name']] 
    df_3 = df_2[(df_2['film'] == pelicula)]
    df = df_3.groupby(['year_ceremony','category','name','film','win']).agg('count')
    df.reset_index().to_csv('../output/movie/resumenPelicula.csv', index=False)
    df.to_html('../input/resumenPelicula.html')
    return df.reset_index()
