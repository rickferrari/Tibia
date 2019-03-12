    #IMPORTS
import requests
from bs4 import BeautifulSoup
####import pandas as pd
from datetime import datetime
import sqlite3

    #Data e hora de extração
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S, %A")

    #Criando variaveis
worlds = []
lists = []
url = []
magic = []

    #Conectando a base de dados
conn = sqlite3.connect('tibia.db')
cursor = conn.cursor()

    #Coletando dados do SQL
cursor.execute("select World from world_list")
worldsRow = cursor.fetchall()
w=0
for cRow in worldsRow:
        worlds.append((worldsRow[w][0]).replace(u' ', '+'))
        w+=1
        
cursor.execute("""select nome from category where nome='magic'""")
listsRow = cursor.fetchall()
####l=0
####for lRow in listsRow:
####        lists.append((listsRow[l][0]).replace(u' ', '+'))
####        l+=1
lists = listsRow[0][0]

        #Montando URL de extração
urli = 'https://secure.tibia.com/community/?subtopic=highscores&world='
ulist = '&list=' # Skills: 0-achievements, 1-axe , 2-club, 3-distance, 4-experience, 5-fishing,
                         # 6-fist, 7-loyalty, 8-magic, 9-shielding, 10-sword
uprof = '&profession=' # 0-ALL, 1-Knights, 2-Paladins, 3-Sorcerers, 4-Druids
upag = '&currentpage=' # Páginas até 12.

for w in worlds:
        for p in range(1,13): # Definindo as páginas de extração, até 12 (marcar 13 no range)
            url.append(urli +w+ '&list=' +lists+ '&profession=' +str(2)+ '&currentpage=' +str(p))

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
        ####r = requests.get(u)
        soup = BeautifulSoup(r.text, 'html.parser')
        table = soup.find('table', attrs={'class':'TableContent'})
        rows = table.find_all('tr')

        #Pasando pelas linhas e agrupando em uma lista
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
                    magic.append([ele for ele in cols if ele]) #Livrar-se de valores vazios
        lista = list(magic)

        #Inset data in table
cursor.execute("""DELETE FROM top_magiclevel""")
conn.commit()
cursor.execute("""UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='top_magiclevel';""")
conn.commit()
for dmain in magic:
        ####print(dmain)
        cursor.execute("""
        INSERT INTO top_magiclevel (Rank, Name, Vocation, Level, World, Link, Extract_data)
        VALUES (?,?,?,?,?,?,?)""",(dmain))
conn.commit()
print('Dados inseridos com sucesso.')
conn.close()