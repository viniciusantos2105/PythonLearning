import json

with open("bd.json", "r") as arq_json:
    dicionario = json.load(arq_json)
    print(dicionario)