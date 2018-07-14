import sqlite3

# conectando...
conn = sqlite3.connect('tibia.db')
# definindo um cursor
cursor = conn.cursor()

#INSERIR CAST**

#Dropando tabela (CASO TENHA NECESSIDADE)
cursor.execute("""
Drop TABLE  if exists top_sword 
""")
conn.commit()
print('Tabela dropada com sucesso.')


# criando a tabela top_sword (schema)
cursor.execute("""
CREATE TABLE if not exists top_sword (
    id INTEGER  PRIMARY KEY AUTOINCREMENT NOT NULL,
    Rank INTEGER  NULL,
    Name VARCHAR(30)  NULL,
    Vocation VARCHAR(20)  NULL,
    Level INTEGER  NULL,
    World VARCHAR(25)  NULL,
    Link VARCHAR(100) NULL,
    Extract_data TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);
""")
conn.commit()
print('Tabela top_sword criada com sucesso.')


# desconectando...
conn.close()
