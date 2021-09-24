#!/usr/bin/python3

# json tem cara de dicionario

import json
with open('arquivo.json') as arquivo:
    conteudo = json.load(arquivo)

# verificar o tipo de dado

print(type(conteudo))

# trata como for um dicionario

for key in conteudo.keys():
    print(key)

# para salvar o json

dic = {'nome': 'Cleomar Schmitzhaus', 'idade': 29}
with open('nome_do_arquivo.json', 'x') as arquivo:
    json.dump(dic, arquivo, ensure_ascii=False)

exit()