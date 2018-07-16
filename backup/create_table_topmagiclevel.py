# 02_create_schema.py
import sqlite3

# conectando...
conn = sqlite3.connect('tibia.db')
# definindo um cursor
cursor = conn.cursor()

#INSERIR CAST**

#Dropando tabela (CASO TENHA NECESSIDADE)
cursor.execute("""
Drop TABLE top_magiclevel 
""")
conn.commit()
print('Tabela dropada com sucesso.')


# criando a tabela top_magiclevel (schema)
cursor.execute("""
CREATE TABLE top_magiclevel (
        id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Rank   integer,
        Name   VARCHAR(30),
        Vocation  VARCHAR(20),
        Level    integer,
        World    VARCHAR(25),
        Link VARCHAR(100) NULL,
        Extract_data [timestamp] NOT NULL
);
""")
conn.commit()
print('Tabela top_magiclevel criada com sucesso.')




# desconectando...
conn.close()
