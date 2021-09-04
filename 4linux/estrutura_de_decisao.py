#!/usr/bin/python3

# Apliacação menu interativo

# Laço indefinido

contador = 0

while contador < 100:
    print(contador)
    # contador =+ 1
    # contador = contador + 1
    break

print(contador)

####################################

# Apliacação menu interativo

# enquanto 1 == 1:...
while True:
    op = input('Digite a opção desejada:\n1- Saudação\n2- Sair\n3- nenhuma das anteriorers\n')

    if op == '1':
        print('Uma saudação qualquer')
    elif op == '2':
        print('Preciso achar uma forma de sair')
        break # opção para sair do script
    elif op == '3':
        continue # opção de continuar, usado para testes
    else:
        print('Opção invalida')

print ('fim')

exit()

# Aplicação de filtros

texto = """

O rato roeu a roupa do rei de roma

"""

# Quantas vezes aparecem as vogais no texrto

vogal = 0

for caractere in texto:
    if caractere.lower() in 'aeiou':
        vogal += 1

print('total de vogais: {}'.format(vogal))

# Qual o numero de vezes que a consoante R aparece no texto

erres = 0

for caractere in texto:
    if 'r' in caractere.lower():
        erres += 1

print('O texto possui {} caracteres \'r\' '.format(erres))

exit()

# Problema: Totalizar o carrinho de compras e aplicar 10% de desconto ao item camiseta

lista_de_compras = [
    ('camiseta', 19.90),
    ('calça Jeans', 20.50),
    ('Meia G', 5.90)
]

total = 0
desconto = 0.9

for compra in lista_de_compras:
    # if compra[0] == 'camiseta':
    if 'camiseta' in compra[0].lower():
        total += compra[1] * desconto
    else:
        total +=compra[1]

print(f'Valor total da compra:  {total:.2f}')

exit()

# Lista de compras

lista_de_compras = [
    ('camiseta', 19.90),
    ('calça Jeans', 20.50),
    ('Meia G', 5.90)
]

# Problema: Qul é o total desse carrinho de compras?
# tupla[0] => nome do item
# tupla[1] => Preço

#1: tamanho da lista
# com while

# 1 definir variavel de controle
indice = 0
# 2 definiu uma variavel para armazenar o total
total_de_compras = 0

# 3 percorrer cada item da lista
while indice < len(lista_de_compras):
# 3.1 Acessamos o valor de preço de cada item e acumulamos na variavel total_de_compras
    total_de_compras += lista_de_compras[indice][1]
    indice += 1

print(f'O total de compras é : {total_de_compras}')

# com for

total = 0

for compra in lista_de_compras:
    total += compra[1]

# 1 compra = lista_de_compra[0]
# total += compra[1]
# 2 compra = litsa_de_compra[1]
# total += compra[1]

exit()

# Como acessar dicionario

dicionario = {
    'nome': 'Cleomar',
    'idade': '29',
    'dados': '[0,1,2,3,4]',
    'tupla': '(0,1,2,3, 55)'
}

print(dicionario['tupla']) # (0,1,2,3)
print(dicionario['tupla'][-1]) # 2

# (nome, 'idade', 'dados', 'tupla')
for chave in dicionario.keys():
    if chave == 'idade':
        print(f'ACHEI - ', dicionario[chave])

# Cleomar, 29, [1,2,3,4], (0,1,2,3, 55)
for valor in dicionario.values():
    if valor == '29':
        print(f'achei a idade')
                # [('nome', 'Cleomar'), ('idade', 29), ('dados', [0,1,2,3,4]), ('tupla', (0,1,2,3,55))]
for chave, valor in dicionario.items():
    print(f'key: {chave} - value: {valor}')

a,b,c = 1,2,3
print(f'a => {a} - b => {b} - c =>{c}')

exit()

# Revisar Tuplas/lista

lista = [0,1,2,3, ('11-12-2020', 88.50), [5,6,7,8]]

print(lista[0])      # 0
print(lista[-1])     # [5,6,7,8]
print(lista[-1][2])  # 7

matriz = [
    [ 0, 1, 2 ], # 0 - linha 1
    [ 3, 4, 5 ], # 1 - linha 2
    [ 6, 7, 8 ]  # 2 - linha 3
#     0  1  2
#    c1 c2 c3
]

print('tamanho de linhas matriz:', len(matriz))

soma = 0

for linha in range(len(matriz)): #loop de linhas
    for coluna in range(len(matriz[linha])):
        soma += matriz[linha][coluna]

print(soma)

exit()

# for

# não precisa ter variavel de controle
# Para cada "num" no meu intervalo (0,201) eu apresento "num"

for num in range (0,201):
    print(num)
    # print(num**2) numero ao quadrado

exit()

# While = repetição

# python possui 2 modelos de estrutuera de repetição
# while = 'enquanto'
# enquanto uma condição não é feita, repete
# variavel de controle
# passos

numero = 0

while numero <=100:
    print(numero)
    numero = numero + 1
    # numero += 1

print('fim do loop')

exit()

#Dicionarios = hash
# Nunca vai no numero da pagina, vc busca pela letra de depois a palavra
# No dicionario as informaçõpes são mais implicitas
# dicionario usa a marcão = {}

dicionario = {} # vc deve definir que é um dict class 'dict'

# dicionario = ['nome'] = 'Cleomar Schmitzhaus'
dicionario

# Acessa o dicionario apartir da palavre chave: dicionario['nome']
# armazena dados por chave e valor

# Para add valor dentro do dicionario
dicionario['idade'] = 29

# para remover algum dado dentro do dicionario
del dicionario['idade']

dicionario.values() #Retorna os valores das chaves

dicionario.get('nome') #tem segurança, caso não existe o dado ele retorna #KeyError

# dicionario.pop('idade') remove e te mostra oq removeu

# JSON transita informações dentre linguagens e APIs
# JSON é um dicionário

exit()

# tuplas usa a marcação de "()"
tupla = (0, 1, 2, 3, 4)
print(tupla)

# Tupla é um tipo imutavel
# id(tupla) mostra o id dela, quando nova, ele exclui a velha e cria um novo id
# tuplas foram criadas para representar determinada linha, manejo de hardware e consumo, menos consumo

tupla2 = ('julio', 34, 12345667890)
# vc deve conhecer a estrutura

nome, idade, cpf = tupla2
print(tupla2)
print(cpf)
print(nome)
print(idade)

exit()

# Lista/Tuplas = Coleções

from typing import List

lista = [0, 1, 2, 3, 4, 5, "texto", 1.5, [0, 1, 2, 3]]
# Para add um novo valor no final da lista = lista.append('Novo Item')
# [1, 2, 3, 4, 5, "texto", 1.5, [0, 1, 2, 3], 'Novo Item']

print(lista)
print(lista[-1])

lista.pop()
# Remove o ultimo elemento e mostra oq removeu
List.remove([...])
# Remove elemento expecifico dentro de []

#para ver manual
# help(lista.remove)
# help(lista.pop) ...

del lista[-1]
# para remover conteudo da lista

exit()

# Decisões alinhadas ou decisões em sequencia
# Calculo do IMC

# 1 capturar as informações de peso e altura
peso = float(input('Digite seu peso '))
altura = float(input('Digite sua altura '))

# 2 Calcular o indice do IMC
imc = peso / (altura ** 2)

# 3 Classificar o IMC
if imc < 18.5:
    print(f'Baixo Peso - IMC: {imc:.2f}') #f = strg # formatação de numeros depois do 0 ":.2f"
elif imc < 24.9:
    print(f'Normal - IMC: {imc:.2f}')
elif imc <29.9:
    print(f'Pré obesidade - IMC: {imc:.2f}')
elif imc < 34.9:
    print(f'Obesidade Grau I - IMC: {imc:.2f}')
elif imc < 39.9:
    print(f'Obesidade grau II - IMC: {imc:.2f}')
else:
    print(f'Obesidade grau III - IMC: {imc:.2f}')

# Numero de classificações - 1 -> de 6 Valida 5 e cai na ultima caso necessário

exit()

# Operadores de pertencimento

texto = 'um qualquer texto'
'qualquer' in texto #True
'XXXX' in texto #False
'XCVFD' not in texto #True

texto.split()
# ['um', 'texto', 'qualquer']
# 'um' in texto.split()
#True

exit()

# Operadores logicos

# Tipo buleano, que é um resultado de uma operação logica
# True e False

# and -> necessita que os dois parametros sejam verdadeiros
(5 >= 5) and (4 > 3) # se ambas são verdadeiras dai é True
(5 < 3) and (7 == 3) # False

# True and True => True
# True and False => False
# False and True => False
# False and False => False

# not inverte o resultado de False = True,  ou True = False
5 > 5 #False
not 5 > 5 #True
5 == 5 # para trabalhar com igauldade
'Esse texto' != 'outro texto' #True
'Esse texto' == 'outro texto' #False
'Esse texto' == 'Esse texto' #True

exit()

# Operadore aritmeticos

texto = 'um texrto qualquer'
texto * 2 # vai repetir duas vezes o texto
outro_texto = '10'
texto + outro_texto #concatenar valores de str
#texto + 10 vai da erro de sintaxe
# texto so trabalha com +

contador = 0
contador = contador + 1
print(contador)

# tambem funciona
contador += 1
contador -= 1
contador *= 2 # muda para tipo float
contador /= 2 # muda para tipo float

exit()

# string

texto = 'Cleomar Schmitzhaus'

outro_texto = "tanto faz se é simples ou dupla"

frase = """
Isso é uma frase muito longa mesmo que contem caracteres especias como essas aqui .,.;=[]
"""

caracters_especiais = '\\n'
print(caracters_especiais)

caracters_especiais = '\\n'
print(caracters_especiais) # pula a linha

print('\t isso é um tab')

print('\tt isso é dois tabs')

# anotação cientifica
# para pegar um caracter especifico
texto[3] # = e
texto[1] # = C
texto[-1] # pega o ultimo caracter da string

# Capturar intervalos de forma reversa
texto[-1:0:-1] # de traz pra frente a string

# sequencias de funcoes
texto.FUNCAO() # ver opções de comandos .FUNCAO

#string é um tipo especial de dado

exit()




# tipos de dados numericos

inteiro = 15
string = '15'
decimais = 10.52 #vai associar numero quebrado com o "."
padrao_br = 10,5 # Vai ser uma tupla
complexo = 5 + 5j # numeral complexo, e é pouco usado
# + - * / ** // %

num1 = 10
num2 = 3
resultado = num1 + num2

num1 * num2

num1 ** num2

2 ** 3 ** 2 # <- da esquerda para a direita

num1 / num2 # resultado sempre vai ser um float

5 // 2  # so mostra a parte inteira
5 % 2 # vai apresentar somente o resto da divisão


# List, tuplas
# dicionarios
exit()