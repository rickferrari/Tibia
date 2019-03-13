    # IMPORTS
from datetime import datetime
import sqlite3

    # Data e hora de extração
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S, %A")

    # Criando variaveis
worlds = []
lists = []
url = []
voc1 = []
Vocations = {0:'ALL', 1:'Knights', 2:'Paladins', 3:'Sorcerers', 4:'Druids'}
Categorys = {0:'achievements', 1:'axe', 2:'club', 3:'distance', 4:'experience',
             5:'fishing', 6:'fist', 7:'loyalty',8:'magic', 9:'shielding', 10:'sword'}


    # Conectando a base de dados
conn = sqlite3.connect('tibia.db')
cursor = conn.cursor()

    # Limpando a tabela
cursor.execute(""" Drop TABLE if exists url_Extrations """)
conn.commit()
        ## criando a tabela world_list (schema)
cursor.execute("""
CREATE TABLE if not exists url_Extrations (
    id INTEGER  PRIMARY KEY AUTOINCREMENT NOT NULL,
    World VARCHAR(25)  NULL,
    Category VARCHAR(25) NULL,
    VocationID VARCHAR(20)  NULL,
    VocationNAME VARCHAR(20)  NULL,
    Link VARCHAR(100)  NULL,
    Extract_data TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);
""")
conn.commit()

        # COMEÇANDO A TRABALHAR OS DADOS

    # Coletando dados do SQL
cursor.execute("""select World from world_list""")
worldsRow = cursor.fetchall()
w = 0
for cRow in worldsRow:
    worlds.append((worldsRow[w][0]).replace(u' ', '+'))
    w += 1

cursor.execute("""select nome from category""")
listsRow = cursor.fetchall()
l=0
for lRow in listsRow:
    lists.append((listsRow[l][0]).replace(u' ', '+'))
    l+=1

    # Montando URL de extração
urli = 'https://secure.tibia.com/community/?subtopic=highscores&world='
ulist = '&list='    #### Skills: 0-achievements, 1-axe , 2-club, 3-distance, 4-experience, 5-fishing,
                    ####         6-fist,         7-loyalty,      8-magic,    9-shielding, 10-sword
uprof = '&profession='  #### 0-ALL, 1-Knights, 2-Paladins, 3-Sorcerers, 4-Druids
upag = '&currentpage='  #### Páginas até 12.

for w in worlds:
    for l in lists:
        for voc in range(0,5):
            for pg in range(1, 13):  # Definindo as páginas de extração, até 12 (marcar 13 no range)
                voc1 = Vocations[voc]
                url.append( [w]
                           +[l]
                           +[voc]
                           +[voc1]
                           +[(urli + w + '&list=' + l + '&profession=' + str(voc) + '&currentpage=' + str(pg))])

    # Inset data in table
cursor.execute("""DELETE FROM url_Extrations""")
conn.commit()
cursor.execute("""UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='url_Extrations';""")
conn.commit()
for dmain in url:
        ####print(dmain)
        cursor.execute("""
        INSERT INTO url_Extrations (World,Category,VocationID,VocationNAME,Link,Extract_data)
        VALUES (?,?,?,?,?,?)""",(dmain[0],dmain[1],dmain[2],dmain[3],dmain[4],now))
conn.commit()
print('Dados inseridos com sucesso.')
conn.close()