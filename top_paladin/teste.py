# IMPORTS
import requests
from bs4 import BeautifulSoup
####import pandas as pd
from datetime import datetime
import sqlite3

# Data e hora de extração
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S, %A")

# Criando variaveis
worlds = []
lists = []
url = []

    # Conectando a base de dados
conn = sqlite3.connect('../tibia.db')
cursor = conn.cursor()

    # Coletando dados do SQL
#cursor.execute("select World from world_list")
#worldsRow = cursor.fetchall()
#w = 0
#for cRow in worldsRow:
#    worlds.append((worldsRow[w][0]).replace(u' ', '+'))
#    w += 1

cursor.execute("""
        SELECT Link FROM url_Extrations
        WHERE
              Category = 'distance'
          and VocationNAME = 'Paladins'
        """)
urlRow = cursor.fetchall()
ul = 0
for cRow in urlRow:
    url.append(urlRow[ul][0])
    ul += 1
print(len(url))