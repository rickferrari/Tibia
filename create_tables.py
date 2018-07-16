import sqlite3

    # conectando a base
conn = sqlite3.connect('tibia.db')
    # definindo um cursor
cursor = conn.cursor()

#INSERIR CAST**

    #Renovando a tabela. Drop da tabela para ser recriada (Forma de truncar)
cursor.execute(""" Drop TABLE if exists world_list """)
cursor.execute(""" Drop TABLE if exists category """)
cursor.execute(""" Drop TABLE if exists top_distance """)
cursor.execute(""" Drop TABLE if exists top_magiclevel """)
cursor.execute(""" Drop TABLE if exists top_shielding """)
cursor.execute(""" Drop TABLE if exists top_achievements """)
cursor.execute(""" Drop TABLE if exists top_loyalty """)
cursor.execute(""" Drop TABLE if exists top_fist """)
cursor.execute(""" Drop TABLE if exists top_club """)
cursor.execute(""" Drop TABLE if exists top_sword """)
cursor.execute(""" Drop TABLE if exists top_axe """)
cursor.execute(""" Drop TABLE if exists top_fishing """)
cursor.execute(""" Drop TABLE if exists top_experience """)
conn.commit()
#print('Tabela dropada com sucesso.')

        #Criando tabelas...

    # criando a tabela world_list (schema)
cursor.execute("""
CREATE TABLE if not exists world_list (
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

    # criando a tabela category (schema)
cursor.execute("""
CREATE TABLE if not exists category
(
	id INTEGER  PRIMARY KEY AUTOINCREMENT NOT NULL,
	Name VARCHAR(20),
	Extract_data TIMESTAMP default CURRENT_TIMESTAMP not null
);
""")

#### ACHAR UMA FORMA DE CHAMAR A CRIAÇÃO DAS CATEGORIAS (INSERT TABLES)
#### IMPORT CREATE_TABLE_CATEGORY


    # criando a tabela top_distance (schema)
cursor.execute("""
CREATE TABLE if not exists top_distance (
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

    # criando a tabela top_magiclevel (schema)
cursor.execute("""
CREATE TABLE if not exists top_magiclevel (
        id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Rank   integer,
        Name   VARCHAR(30),
        Vocation  VARCHAR(20),
        Level    integer,
        World    VARCHAR(25),
        Extract_data [timestamp] NOT NULL
);
""")

cursor.execute("""
CREATE TABLE if not exists top_shielding (
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

# TROCAR LEVEL POR POINTS
    # criando a tabela top_achievements (schema)
cursor.execute("""
CREATE TABLE if not exists top_achievements (
    id INTEGER  PRIMARY KEY AUTOINCREMENT NOT NULL,
    Rank INTEGER  NULL,
    Name VARCHAR(30)  NULL,
    Vocation VARCHAR(20)  NULL,
    Points INTEGER  NULL,
    World VARCHAR(25)  NULL,
    Link VARCHAR(100) NULL,
    Extract_data TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);
""")

#Rank,Name,Vocation,Title,Points
    # criando a tabela top_loyalty (schema)
cursor.execute("""
CREATE TABLE if not exists top_loyalty (
    id INTEGER  PRIMARY KEY AUTOINCREMENT NOT NULL,
    Rank INTEGER  NULL,
    Name VARCHAR(30)  NULL,
    Vocation VARCHAR(20)  NULL,
    Title VARCHAR(25)
    Points INTEGER  NULL,
    World VARCHAR(25)  NULL,
    Link VARCHAR(100) NULL,
    Extract_data TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);
""")

    # criando a tabela top_fist (schema)
cursor.execute("""
CREATE TABLE if not exists top_fist (
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

    # criando a tabela top_club (schema)
cursor.execute("""
CREATE TABLE if not exists top_club (
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

    # criando a tabela top_axe (schema)
cursor.execute("""
CREATE TABLE if not exists top_axe (
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

    # criando a tabela top_fishing (schema)
cursor.execute("""
CREATE TABLE if not exists top_fishing (
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

#Rank,Name,Vocation,Level,Points
    # criando a tabela top_experience (schema)
cursor.execute("""
CREATE TABLE if not exists top_experience (
    id INTEGER  PRIMARY KEY AUTOINCREMENT NOT NULL,
    Rank INTEGER  NULL,
    Name VARCHAR(30)  NULL,
    Vocation VARCHAR(20)  NULL,
    Level INTEGER  NULL,
    Points INTEGER  NULL,
    World VARCHAR(25)  NULL,
    Link VARCHAR(100) NULL,
    Extract_data TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);
""")

conn.commit()
#print('Tabelas criadas com sucesso.')

# desconectando e liberando a base de dados
conn.close()
