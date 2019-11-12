def urlWiki(string):
    result = ''
    for i in string.split(' '):
        result += ('_'+i)
    url= 'https://en.wikipedia.org/wiki/{}'.format(result.strip('_'))
    return url

def infoGeneral(soupW):
    # print ('Name: ',soupW.find('tbody').find_all('tr')[2].find('div', {'class':"nickname"}).text.strip())
    print ('Birth date: ',soupW.find('tbody').find_all('tr')[2].find('span', {'class':"bday"}).text.strip())
    print ('Birth place :',soupW.find('tbody').find_all('tr')[2].find('div', {'class':"birthplace"}).text.strip())
