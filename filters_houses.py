    #IMPORTS
import requests
from bs4 import BeautifulSoup
####import pandas as pd
from datetime import datetime
import sqlite3
import time

    # Data e hora de extração
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S, %A")

    # Criando variaveis
worlds = []
url = []
City = []
State = []
Order = []
Type = []
Colns = []

###world = Mundo
###town  = Cidade
###state = checked, auctioned, rented
###order = checked, size, rent, bid, end
###type = houses, guildhalls

    # Conectando a base de dados
conn = sqlite3.connect('tibia.db')
cursor = conn.cursor()

    # Coletando dados do SQL
cursor.execute("select World from world_list")
worldsRow = cursor.fetchall()
w=0
for cRow in worldsRow:
        worlds.append((worldsRow[w][0]).replace(u' ', '+'))
        w+=1

        #Montando URL de extração
urli = 'https://www.tibia.com/community/?subtopic=houses'
uworld = '&world='
utown = '&town=' # Citys of tibia

        #SOUP
r = requests.get(urli)
tentativa = 0
while r.status_code != 200:
        if tentativa > 10:
            print("Não foi possível carregar a página :" + str(urli))
            break
        r = requests.get(urli)
        tentativa += 1
        print ("Erro. Tentando novamente")
soup = BeautifulSoup(r.text, 'html.parser')
table = soup.find('form', attrs={'action':'https://www.tibia.com/community/?subtopic=houses'})
rows = table.find_all('input', attrs={'name':'town'})

# Pasando pelas linhas e agrupando em uma lista as cidades
rows = table.find_all('input', attrs={'name': 'town'})
for row in rows:
    City.append(row['value'])

    # Pasando pelas linhas e agrupando em uma lista as os states
rows1 = table.find_all('input', attrs={'name': 'state'})
for row1 in rows1:
    State.append(row1['value'])

    # Pasando pelas linhas e agrupando em uma lista as os order
rows2 = table.find_all('input', attrs={'name': 'order'})
for row2 in rows2:
    Order.append(row2['value'])

    # Pasando pelas linhas e agrupando em uma lista as os type
rows3 = table.find_all('input', attrs={'name': 'type'})
for row3 in rows3:
    Type.append(row3['value'])

rows9 = table.find_all('td', attrs={'valign':'top'})

#urli + uworld + utown
#for w in worlds:
#    for c in City:
#        for s in State:
#            for o in Order:
#                for t in Type:
#                    #Colns.append(w,c,s,o,t)
#                    print('Mundo {}, Cidade {}, State {}, Sort {}, Type {}'.format(w, c, s, o, t))

        #Inset data in table
cursor.execute("""DELETE FROM Filters_Houses""")
conn.commit()
cursor.execute("""UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='Filters_Houses';""")
conn.commit()
for w in worlds:
    for c in City:
        cursor.execute("""
        INSERT INTO Filters_Houses (World, Town, Link, Extract_data)
        VALUES (?,?,?,?)""",(w,c,urli+uworld+w+utown+c,now))
conn.commit()
print('Dados inseridos com sucesso.')
conn.close()