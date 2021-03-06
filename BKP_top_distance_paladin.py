    #IMPORTS
import requests
from bs4 import BeautifulSoup
####import pandas as pd
from datetime import datetime
import sqlite3

    # Data e hora de extração
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S, %A")

    # Criando variaveis
worlds = []
lists = []
url = []
distance = []
Extrations = []

    # Conectando a base de dados
conn = sqlite3.connect('tibia.db')
cursor = conn.cursor()

    # Coletando dados do SQL

cursor.execute("""Select Link from url_Extrations WHERE VocationNAME = 'Paladins'""")
urlRow = cursor.fetchall()
ui=0
for cRow in urlRow:
        url.append((urlRow[ui][0]).replace(u' ', '+'))
        ui+=1
#print(url)


##########################################################################################
cursor.execute("select World from world_list")
worldsRow = cursor.fetchall()
w=0
for cRow in worldsRow:
        worlds.append((worldsRow[w][0]).replace(u' ', '+'))
        w+=1
#
#   cursor.execute("""select nome from category where nome='distance'""")
#   listsRow = cursor.fetchall()
#   ####l=0
#   ####for lRow in listsRow:
#   ####        lists.append((listsRow[l][0]).replace(u' ', '+'))
#   ####        l+=1
#   lists = listsRow[0][0]
##########################################################################################

        #SOUP
for u in url:
        tentativa = 0
        r = requests.get(u)
        while r.status_code != 200:
                if tentativa > 10:
                    print("Não foi possível carregar a página :" + str(u))
                    break
                r = requests.get(u)
                tentativa += 1
                print ("Erro. Tentando novamente")
        #### r = requests.get(u)
        soup = BeautifulSoup(r.text, 'html.parser')
        table = soup.find('table', attrs={'class':'TableContent'})
        rows = table.find_all('tr')

        ## Pasando pelas linhas e agrupando em uma lista
        for row in rows: #Organizando as linhas da extração
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            for w in worlds:
                    if w in u:
                            cols.append(w) #Insere world
                            break
            cols.append('https://secure.tibia.com/community/?subtopic=characters&name='+(cols[1].replace(u' ', '+')))
            cols.append(now) #Insere a data de extração em cada linha
            if len(cols[0]) < 3: #Eliminando a linha de "titulo"
                    distance.append([ele for ele in cols if ele]) #Livrar-se de valores vazios
        lista = list(distance)

        #Inset data in table
cursor.execute("""DELETE FROM top_distance""")
conn.commit()
cursor.execute("""UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='top_distance';""")
conn.commit()
for dmain in distance:
        ####print(dmain)
        cursor.execute("""
        INSERT INTO top_distance (Rank, Name, Vocation, Level, World, Link, Extract_data)
        VALUES (?,?,?,?,?,?,?)""",(dmain))
conn.commit()
print('Dados inseridos com sucesso.')
conn.close()