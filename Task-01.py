import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url='https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
req= requests.get(url)

soup=BeautifulSoup(req.text,'html.parser')             
table=soup.find_all("table")[2]

                
world_titles=table.find_all('th')     
world_table_titles=[title.text.strip() for title in world_titles]
world_table_titles=world_table_titles[:2]+ world_table_titles[-4:-2]
print(world_table_titles)

df=pd.DataFrame(columns=world_table_titles)


column_data=table.find_all('tr')
for row in column_data[3:]:                                                          
    row_data=row.find_all('td')
    indi_row_data=[data.text.strip() for data in row_data]
    fin=indi_row_data[:2]+indi_row_data[-4:-2]
    print(fin)
    length=len(df)
    df.loc[length]=fin
    
#data frame
print(df)

#cleaning data
df['Estimate'] = df['Estimate'].str.replace(r'\[.*\]', '', regex=True)
df['Year'] = df['Year'].str.replace(r'\[.*\]', '', regex=True)
df.drop_duplicates()
df.dropna(axis=0,how='any',inplace=False)

#histogram
plt.figure(figsize=(13, 7))
plt.hist(df['Estimate'], bins=100, edgecolor='black')
plt.title("List of countries by GDP in 2023")
plt.xlabel("GDP (nominal)")
plt.ylabel("Frequency")
plt.show()


