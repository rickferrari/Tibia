# 02_create_schema.py
import sqlite3

# conectando...
conn = sqlite3.connect('tibia.db')
# definindo um cursor
cursor = conn.cursor()

#INSERIR CAST**

#Dropando tabela (CASO TENHA NECESSIDADE)
cursor.execute("""
Drop TABLE char_infor 
""")
conn.commit()
print('Tabela dropada com sucesso.')


# criando a tabela char_infor (schema)
cursor.execute("""
CREATE TABLE [char_infor] (
[id] INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT,
[Name] VARCHAR(30)  NULL,
[Sex] VARCHAR(10)  NULL,
[Vocation] VARCHAR(20)  NULL,
[Level] INTEGER  NULL,
[Achievement] INTEGER  NULL,
[World] VARCHAR(25)  NULL,
[Residence] VARCHAR(30)  NULL,
[House] VARCHAR(80)  NULL,
[Last_Login] VARCHAR(80)  NULL,
[Account_Status] VARCHAR(30)  NULL,
[Loyalty_Title] VARCHAR(30)  NULL,
[Extract_data] timestamp DEFAULT CURRENT_TIMESTAMP NOT NULL
);
""")
print('Tabela char_infor criada com sucesso.')




# desconectando...
conn.close()
