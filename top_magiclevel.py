    #IMPORTS
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import sqlite3
##import worlds_list.py #import list of world

    # Data e hora de extração
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S, %A")

        # Criando variaveis
worlds = []
url = []
magiclevel = []
uWorlds = ''

    # Load File
##worlds = list(open('mundo_name.txt','r'))
lists = list(open('category.txt','r'))
    # Remove /n
##worlds = [s.rstrip() for s in worlds]
lists = [s.rstrip() for s in lists]


        # Conectando a base de dados
conn = sqlite3.connect('tibia.db')
cursor = conn.cursor()


        # Coletando dados do SQL
cursor.execute("select World from world_list")
worldsRow = cursor.fetchall()
##print(charsrow[1][0])
i=0
for cRow in worldsRow:
        worlds.append((worldsRow[i][0]).replace(u' ', '+'))
        i+=1
##print(worlds)
        

        # Montando link de extração
urli = 'https://secure.tibia.com/community/?subtopic=highscores&world='
ulist = '&list=' # Skills: 0-achievements, 2-axe ,3-club, 3-distance, 4-experience, 5-fishing,
                 # 6-fist, 7-loyalty, 8-magic, 9-shielding, 10-sword
uprof = '&profession=' # 0-ALL, 1-Knights, 2-Paladins, 3-Sorcerers, 4-Druids
upag = '&currentpage=' # Páginas até 12.

for w in worlds:
        for p in range(1,4): # Para distance, pegar apenas a primeira página
            url.append(urli +w+ ulist +lists[8]+ uprof +str(2)+ upag +str(p))

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
                        
##        r = requests.get(u)
        
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
            cols.append(now) #Insere a data de extração em cada linha
            if len(cols[0]) < 3: #Eliminando a linha de "titulo"
                    magiclevel.append([ele for ele in cols if ele]) #Livrar-se de valores vazios
        lista = list(magiclevel)


        ##Inserindo dados nas tabelas
cursor.execute("""DELETE FROM top_magiclevel""")
conn.commit()
cursor.execute("""UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='top_magiclevel';""")
conn.commit()
for dmain in magiclevel:
        cursor.execute("""
        INSERT INTO top_magiclevel (Rank, Name, Vocation, Level, World, Extract_data)
        VALUES (?,?,?,?,?,?)""",(dmain))
conn.commit()
print('Dados inseridos com sucesso.')
conn.close()
