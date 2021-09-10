#!/usr/bin/python3

import random

# lista com varias pessoas cadastradas:
# sorteio

lista = [
    ('123456','jão'),
    ('347673','cleomar'),
    ('546456','Camila'),
    ('867786','Maria'),
    ('756756','Jovana'),
    ('034554','Fernando')
]

primeiro = lista[random.randint(0, len(lista)-1)]
# embaralhar = lista[random.shuffle(lista)]

print(primeiro) 
# print(embaralhar)

# Random para games
# Dança das cadeiras com random

num_cadeiras = len(lista) -1

while num_cadeiras > 1:
    print('musica tocando')
    print('musica parou')
    print('jogadores se movimentam')

# sortear alguem para sair do jogo

    random.shuffle(lista)
    print(f"O jogador {lista.pop()} saiu do jogo!")

# segunda forma:

# num_participantes = len(lista)-1
# indici_saida = random.randint(0,num_participantes)
# del lista[indici_saida]

exit()