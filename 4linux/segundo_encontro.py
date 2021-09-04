#!/usr/bin/python3

# aulda 3 de 4
# [X] Funções
# [] Modulos
# [] Arquivos
# [] OOP

#  Olhei até os 38 minutos

# Modulos



exit()

# Função

num1 = 10
num2 = 35

def funcao_qualquer(num1, num2): #Call operator
    # pass # <- ignorar/ir para a proxima função
    # print(num1+num2) # para imprimir a soma
    return num1 + num2 # para retornar valor em memoria

def e_maior(num1,num2):
    outra_variavel = 'texto' #essa variavel so aparece aqui dentro
    # variavel global não é recomendado, variavel que aparece sempre se cria constante = em MAIUSCULO
    if num1 >num2:
        return num1
    return num2

CONSTANTE = 20 # constante

def soma_varios_valores(*numeros):
    soma = 0
    print(type(numeros))
    for num in numeros:
        soma += num
    return soma

exit()    