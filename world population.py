import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.worldometers.info/world-population/population-by-country/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify)

rows = soup.find('table', {'id':'example2'}).find('tbody').find_all('tr')
print(len(rows))

#creating an array countries
countries_list = []

for row in rows:
    dic = {}
    dic['Countries'] = row.find_all('td')[1].text
    dic['Population 2024'] = row.find_all('td')[2].text.replace(',','') # replace value to remove , in population like this -> 1,450,935 to 1450935 

    countries_list.append(dic)

print(countries_list[0])

dataframe = pd.DataFrame(countries_list)
dataframe.to_excel('country_population_2024.xlsx', index=False)