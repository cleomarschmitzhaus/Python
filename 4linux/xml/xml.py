#!/usr/bin/python3

# XML

# XML tem estrutura de tag
# bibliotecas XML, tem XML e defusedxml (defusedxml é mais seguro)
# pip3 install defusedxml
# Para acessar a logica é de estrutura de arvore
# deve declarar a ramificação, e depois qual a profundidade

# criar um arquivo apartir do Python

from xml.etree.ElementTree import Comment, Element, SubElement, ElementTree

# Criar estrutura raiz
raiz = Element('partida')

# add elementos

raiz.append(Comment('Partida realizada em 2002')) # Comentario

# Estrutura de tag e texto

ano = SubElement(raiz, 'ano')

# definir o valor do ano = text

ano.text = '2002'

# torneio
torneio = SubElement(raiz, 'torneio')
torneio.text = 'Rio São Paulo'

# tag de times
times = SubElement(raiz, 'times')

mandante =  SubElement(times, 'mandante')
mandante.text = 'Sao Paulo'

visitante = SubElement(times, 'visitante')
mandante.text = 'Palmeiras'

resultado = SubElement(raiz, 'resultado')
resultado.text = '2X4'

# gols mandante

gols = SubElement(resultado, 'gols')
gols_mandante = SubElement(gols, 'mandante')
gols_mandante_jogador1 = SubElement(gols_mandante, 'jogador1')
gols_mandante_jogador1.text = 'França'
gols_mandante_jogador2 = SubElement(gols_mandante, 'jogador2')
gols_mandante_jogador2.text = 'Kaka'

# gols visitantes

gols_visitante = SubElement(gols, 'visitante')
gols_visitante_jogador1 = SubElement(gols_visitante, 'jogador1')
gols_visitante_jogador1.text = 'Magrao'
gols_visitante_jogador2 = SubElement(gols_visitante, 'jogador2')
gols_visitante_jogador2.text = 'Claudecir'
gols_visitante_jogador3 = SubElement(gols_visitante, 'jogador3')
gols_visitante_jogador3.text = 'Alex'
gols_visitante_jogador4 = SubElement(gols_visitante, 'jogador4')
gols_visitante_jogador4.text = 'Arce'

ElementTree(raiz).write('saida.xml')

exit()

from defusedxml import ElementTree as ET
arq_xml = ET.parse('exemplo.xml')

# getrrot posiciona na posição no inicio

raiz = arq_xml.getroot()
for elemento in raiz:
    print(elemento.tag, elemento.text)

# para acessar niveis mais altos

for elemento in raiz.find('times'):
    print(elemento.tag, elemento.text)

#exit()