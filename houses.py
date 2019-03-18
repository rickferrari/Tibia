    #IMPORTS
import requests
from bs4 import BeautifulSoup
####import pandas as pd
from datetime import datetime
import sqlite3

    # Data e hora de extração
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S, %A")

    # Criando variaveis
url = []
house = []

    # Conectando a base de dados
conn = sqlite3.connect('tibia.db')
cursor = conn.cursor()

    # Coletando dados do SQL
cursor.execute("select Link from Filters_Houses WHERE World='Calmera'")
lhouses = cursor.fetchall()
l = 0
for lh in lhouses:
        url.append((lhouses[l][0]).replace(u' ', '+'))
        l+=1
#print(url)

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
        soup = BeautifulSoup(r.text, 'html.parser')
        table = soup.find('div', attrs={'class':'BoxContent'})
        rows = table.find_all('tr')

        ## Pasando pelas linhas e agrupando em uma lista
        for row in rows: #Organizando as linhas da extração
            print(row)
            print('##########################')
            cols = row.find_all('td')
            #cols = [ele.text.strip() for ele in cols]
            #print(cols)
            #print('########################################################')
#            for w in worlds:
#                    if w in u:
#                            cols.append(w) #Insere world
#                            break
#            cols.append(now) #Insere a data de extração em cada linha
            #if len(cols[0]) < 3: #Eliminando a linha de "titulo"
            #        house.append([ele for ele in cols if ele]) #Livrar-se de valores vazios
        #lista = list(house)
print(cols)
#
#        #Inset data in table
#cursor.execute("""DELETE FROM top_distance""")
#conn.commit()
#cursor.execute("""UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='top_distance';""")
#conn.commit()
#for dmain in distance:
#        ####print(dmain)
#        cursor.execute("""
#        INSERT INTO top_distance (Rank, Name, Vocation, Level, World, Link, Extract_data)
#        VALUES (?,?,?,?,?,?,?)""",(dmain))
#conn.commit()
#print('Dados inseridos com sucesso.')
#conn.close()