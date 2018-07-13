# create_schema
import sqlite3

# conectando...
conn = sqlite3.connect('tibia.db')
# definindo um cursor
cursor = conn.cursor()

###Dropando tabela (CASO TENHA NECESSIDADE)
##cursor.execute("""
##Drop TABLE top_distance 
##""")
##print('Tabela dropada com sucesso.')

# criando a tabela world_list (schema)
cursor.execute("""
CREATE TABLE world_list (
        id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        World   VARCHAR(25),
        Online   INTEGER,
        Location  VARCHAR(25),
        PvP_Type    VARCHAR(50),
        BattleEye    VARCHAR(10),
        Additional_Information VARCHAR(50)
        Extract_data [timestamp] NOT NULL
);
""")
print('Tabela world_list criada com sucesso.')


# criando a tabela top_distance (schema)
cursor.execute("""
CREATE TABLE top_distance (
        id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Rank   INTEGER,
        Name   VARCHAR(30),
        Vocation  VARCHAR(20),
        Level    INTEGER,
        world   VARCHAR(25),
        Extract_data [timestamp] NOT NULL
);
""")
print('Tabela top_distance criada com sucesso.')

# criando a tabela top_magiclevel (schema)
cursor.execute("""
CREATE TABLE top_magiclevel (
        id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Rank   integer,
        Name   VARCHAR(30),
        Vocation  VARCHAR(20),
        Level    integer,
        World    VARCHAR(25),
        Extract_data [timestamp] NOT NULL
);
""")
print('Tabela top_magiclevel criada com sucesso.')


# desconectando...
conn.close()
