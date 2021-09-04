#!/usr/bin/python3

# Paradigma estruturado
# Paradigma funcional
# Funções bibliotecas padrão/nativas
# para usar um modulo que não é padrão
# import random
# import os
# random.randint(1,100)) # numero randomico de 1 a 100
# os.system('1s') # para executar algum comando do linux
# parametros
# def nome_da_funcao(param1, param2, param3): # call operator #: -> pertence a estrutura
# instrucões da função
# pass # vai pra proxima
# dados anonimos
# não precisa notação expecifica, vai ser um tipo de notação lambda
# cria função dentro de uma atribuição de varoáveis sem definir ela no script de código

soma = lambda x,y: x + y
print(soma(10,20)) # se torna uma função
res = soma(5,6)

# restrições: deve ser uma instrução curta, somente 1 instrução por vez
# é usado para criar função auxiliar
# envia função como parametro









exit()

# Dados mutaveis mantem o mesmo numero de ID

n1, n2, n3 = 10,20,0

lists = [0,1,2,3,"jujuba"]

dicionario = {}
dicionario['nova_chave']=1

def adicionar_item(lista, item):
    lista.append(item)

adicionar_item(lists, 'macarrão')

exit()

# imutabilidade de dados em python

tupla = (0,1,2,3) # não altera o valor
tupla += 4,5,6,7 # cria uma nova a partir da anterior / vai remover a antiga
inteiros = 1  # imutavel com o mesmo ID
floats = 10.5 # imutavel com o mesmo ID
string = 'texto' # tambem é imutavel

def soma(num1, num2, res):
    res = num1 + num2
    return res

res = 0
num1 = 50
num2 = 20

soma(num1,num2,res)
print(res)
# a = 0
# b = 70
# c = vai acontecer erro
# d = nenhuma das anteriores



exit()

# parametros aula 2

def saudacao():
    print('Ola!') 

def soma(n1, n2):
    return n1 + n2

x = 10
y = 15
print(soma(x,y)) # 25

print(saudacao())

def outra_soma(x1=0, x2=0):
    return x1 + x2

print(outra_soma())
print(outra_soma(33,66))

def multiplicação(n1=1,n2=1):
    return n1 * n2

a = multiplicação(2,4)
b = multiplicação(3)
c = multiplicação()

# somas
# insere somente uma lista (1,2,3,4,5,6,7)

def soma_multiplos_valores(*numeros): # transforma em tupla
    print(type(numeros))
    print(numeros)
    soma = 0
    for num in numeros:
        soma += num

    return soma

# deve inserir chave e valor (num1=1, num2=4, num5=8)
def soma_kwargs(**kwargs): # transforma em dicionário
    print(type(kwargs))
    print(kwargs)

    soma = 0
    for value in kwargs.values():
        soma += value

exit()

print('teste')

# f(x) = x + 1
# f(2) = 2 + 1

def incrementa_um(z = 0): # vira uma variavel de escopo
    res = z + 1
    print(res)

incrementa_um(10)
incrementa_um()

def soma(num1, num2):
    return num1 + num2

x = 5
y = 10
print(soma(x,y))
res = soma(2,2)

#print('valor', sep="")
    #argumento

exit()