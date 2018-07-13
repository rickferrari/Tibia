import sqlite3
from datetime import datetime

    # Data e hora de extração
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S, %A")

    # Conectando a base de dados
conn = sqlite3.connect('tibia.db')
cursor = conn.cursor()

    # Variaveis
lista = ['achievements','axe','club','distance','experience','fishing',
'fist','loyalty','magic','shielding','sword']
a = 'achievements'
##lista.append(now)
        
    #Inset data in table
cursor.execute("""DELETE FROM category""")
conn.commit()
cursor.execute("""UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='category';""")
conn.commit()
for lmain in lista:
##    print(lmain)
    cursor.execute("""INSERT INTO category (Nome,Extract_data) VALUES (?,?)""",(lmain,now))
    conn.commit()
print('Dados inseridos com sucesso.')
conn.close()
