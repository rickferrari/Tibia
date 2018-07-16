import requests 
from bs4 import BeautifulSoup
from datetime import datetime
import sqlite3

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S, %A")
worlds = 'https://secure.tibia.com/community/?subtopic=worlds'

    #Variaveis
world_List = []
colsX = []

    #Conectando a base de dados
conn = sqlite3.connect('tibia.db')
cursor = conn.cursor()

    #SOUP
r = requests.get(worlds)
soup = BeautifulSoup(r.text, 'html.parser')
table = soup.find('div', attrs={'class':'InnerTableContainer'})
rows = table.find_all('tr')

    #Pasando pelas linhas e agrupando em uma lista
for row in rows: #Organizando as linhas da extração
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    cols.append(now) #Insere a data de extração em cada linha
    if len(cols[0]) < 25 and len(cols[1]) < 6: #Eliminando a linha inuteis e linha "titulo
        ####world_List.append([ele for ele in cols if ele]) #Livrar-se de valores vazios
        world_List.append(cols)
        cols[2] = cols[2].replace(u'\xa0', ' ')#.encode('utf-8')
lista = list(world_List)


    #Trabalando com os dados na tabela
cursor.execute("""DELETE FROM world_list""")
conn.commit()
cursor.execute("""UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='world_list';""")
conn.commit()
for dmain in world_List:
        #print(dmain)
        cursor.execute("""
        INSERT INTO world_list (World, Online, Location, PvP_Type, BattlEye, Additional_Information, Extract_data)
        VALUES (?,?,?,?,?,?,?)""",(dmain))
conn.commit()
print('Dados inseridos com sucesso.')
conn.close()