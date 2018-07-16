# 02_create_schema.py
import sqlite3

# conectando...
conn = sqlite3.connect('tibia.db')
# definindo um cursor
cursor = conn.cursor()

#INSERIR CAST**

#Dropando tabela (CASO TENHA NECESSIDADE)
cursor.execute("""
Drop TABLE world_list 
""")
conn.commit()
print('Tabela dropada com sucesso.')


# criando a tabela world_list (schema)
cursor.execute("""
CREATE TABLE world_list (
    id INTEGER  PRIMARY KEY AUTOINCREMENT NOT NULL,
    World VARCHAR(25)  NULL,
    Online INTEGER  NULL,
    Location VARCHAR(25)  NULL,
    PvP_Type VARCHAR(50)  NULL,
    BattlEye VARCHAR(10)  NULL,
    Additional_Information VARCHAR(50)  NULL,
    Extract_data TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);
""")
conn.commit()
print('Tabela world_list criada com sucesso.')




# desconectando...
conn.close()
