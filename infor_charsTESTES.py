    #IMPORTS
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import sqlite3
import urllib.request

    # Data e hora de extração
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S, %A")

    # Criando variaveis
chars = []
url = []
chars0 = []
chars1 = []
chars2 = []
chars3 = []
cc = ['Dudys','Elrik']
#cc = ['Dudys','Lord+Kendo','Lewy','Eagle+Askara','Elrik']

        # Conectando a base de dados
conn = sqlite3.connect('tibia.db')
cursor = conn.cursor()

        # Coletando dados do SQL
cursor.execute("select name from top_distance")
charsRow = cursor.fetchall()
##print(charsRow[1][0])
c=0
for cRow in charsRow:
    ##chars.append((charsRow[c][0]).replace(u' ', '+'))
        chars.append(charsRow[c][0])
        c+=1
##print(chars)


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} # This is chrome, you can set whatever browser you like
##https://secure.tibia.com/community/?subtopic=characters&name=Dudys
urli = 'https://secure.tibia.com/community/?subtopic=characters&name='

for c in cc: #chars:
        url.append(urli + (c.replace(u' ', '+')))
        ##print(url)



        #SOUP

for u in url:
        
        # Criando variaveis de controle
        print(u)
        tentativa = 0

        # Iniciando varredura
        r = requests.get(u)
        while r.status_code != 200:
                if tentativa > 10:
                    print("Não foi possível carregar a página :" + str(u))
                    break
                r = requests.get(u)
                tentativa += 1
                print ("Erro. Tentando novamente")
                
        soup = BeautifulSoup(r.text, 'html.parser')
        ##print (r.status_code) #CODE 200 ELE CONSEGUE ACESSAR A PAGINA (TESTE)
        table = soup.find('div', attrs={'class':'BoxContent'})
        rows = table.find_all('tr')
        
        ## Pasando pelas linhas e agrupando em uma lista
        for row in rows: #Organizando as linhas da extração
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                cols.append(now) #Insere a data de extração em cada linha
                ##if len(cols[0]) < 3: #Eliminando a linha de "titulo"
                ##chars2.append(chars1)
                chars0.append([ele for ele in cols if ele]) #Livrar-se de valores
        if len(chars0) > 0:
                chars1.append(chars0)
        chars0 = []
lista = list(chars0)

#for ux in chars1[4]:
#        if 'Loyalty Title:' not in ux:
#                continue
#        else:
#                print(ux)




uu=(len(chars1)-1)
tt = 0
key = 0
#for i in chars1:
#    tt = 0
#    print(tt)
#    print(len(i))
#    print(i)
#    while tt < len(i):
#        if 'Loyalty Title:' in i[tt]:
#            print(tt)
#            print(i)
#            break
#        if tt == (len(i)-1):
#            print('LIMITE de TT é: {}'.format(tt))
#        print('TT é: {}'.format(tt))
#        tt+=1
#    input('ENTER...')


for i in chars1[0]:
   for uz in chars1[tt]:
        if uz[0] == 'Name:' and uz[1] in chars:
            print(uz[0],uz[1] if len(uz[1]) > 1 else 'null')
            chars2 = []
            chars2.append(uz[0])
            chars2.append(uz[1])
        elif uz[0] in ['Sex:','Vocation:','Level:','Achievement Points:','Residence:','Last Login:','Loyalty Title:']:
            print(uz[0],uz[1] if len(uz[1]) > 1 else 'null')
            chars2.append(uz[0].replace(u'\xa0', ' '))
            chars2.append((uz[1] if len(uz[1]) > 1 else 'NULL').replace(u'\xa0', ' '))
            if uz[0] == 'Last Login:' and uz[0] not in ('Loyalty Title:'):
                chars2.append('Loyalty Title:')
                chars2.append('NOT HAVE')
        #elif 'Loyalty Title:' not in chars1[tt] and uz[0] == 'Last Login:':
        #elif 'Loyalty Title:' not in chars1[tt] and uz[0] in ('Last Login:'):
        #    #print('X')
        #    #if uz[0] in ('Last Login:'):
        #    chars2.append('Loyalty Title:')
        #    chars2.append('NOT HAVE')
   chars3.append(chars2)
   if tt == uu:
       break
   else:
       tt+=1

print('####################################################################')
for i in chars3:
        print(i)
        print('**********************')


        #Inset data in table
##cursor.execute("""DELETE FROM char_infor""")
##conn.commit()
##cursor.execute("""UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='char_infor';""")
##conn.commit()
##for dmain in chars3:
##        print('#################')
##        print(dmain[0],dmain[1],dmain[2],dmain[3],dmain[4],dmain[5],dmain[6],now)
####        print(dmain)
##        cursor.execute("""
##        INSERT INTO char_infor (Name, Sex, Vocation, Level, Achievement, Residence, Last_Login, Extract_data)
##        VALUES (?,?,?,?,?,?,?,?)
##        """,(dmain[0],dmain[1],dmain[2],dmain[3],dmain[4],dmain[5],dmain[6],now))
##conn.commit()
##print('Dados inseridos com sucesso.')
conn.close()


##                        
####lista1 = list(chars2)
####df = pd.DataFrame(chars0)
####print(df)
