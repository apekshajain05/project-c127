import requests
from bs4 import BeautifulSoup
import pandas as pd

starturl='https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'


star_data=[]

page=requests.get(starturl)

soup=BeautifulSoup(page.text,'html.parser')
table=soup.find('table')
table_rows=table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    star_data.append(row)

# print(star_data)

star_names = []
distance =[]
mass = []
radius =[]
lum = []

for i in range(1,len(star_data)):
    star_names.append(star_data[i][1])
    distance.append(star_data[i][3])
    mass.append(star_data[i][5])
    radius.append(star_data[i][6])
    lum.append(star_data[i][7])
    
df = pd.DataFrame(list(zip(star_names,distance,mass,radius,lum)),columns=['Star_name','Distance','Mass','Radius','Luminosity'])
# print(df)

df.to_csv('project-c127.csv')
