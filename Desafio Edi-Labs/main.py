# importando bibliotecas necessárias
from itertools import count
from collections import Counter
import json
from estados import estado
import requests
import csv
import pandas as pd
json_data = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados")
estados = json.loads(json_data.text)
listaEstados = []
cnt = Counter()

newpath = r'C:\Program Files\arbitrary' 
if not os.path.exists(newpath):
    os.makedirs(newpath)

for estadoJson in estados: 
    listaEstados.append(estado(**estadoJson))
    
for estadoObj in listaEstados:
    cnt[estadoObj.nomeRegiao] += 1
    
cnt = dict(cnt)

print(cnt)
df = pd.DataFrame([cnt])

df.to_csv('data.csv',index=False)
print("fim do programa")
