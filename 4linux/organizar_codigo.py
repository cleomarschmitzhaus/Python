#!/usr/bin/python3

def soma(x,y):
    return x+y

# simulação de calculadora
# separar totalmente as funções
# para facilitar a manutenção de codigo

############################################################
#           METODO MAIS COMPLEXO PARA MANUTENÇÂO           #
############################################################

while True: # adicionar um loop

# 1 -  Capturar dois numeros
    n1 = float(input('n1: '))
    n2 = float(input('n2: '))

# 3 - Apresenta opções para o usuário
    print('digite a aopção desejada:\n1- soma\n2- subtração\n3- multiplicação\n4- divisão\n5- sair')

# 2 - Solicita aoo usuário a opção desejada
    op = input('')

# 4 - realizar a operação de acordo com a escolha do usuário
    if op == '1':
        print(n1+n2)
    elif op == '2':
        print(n1-n2)
    elif op == '3':
        print(n1*n2)
    elif op == '4':
        if n2 == 0:
            print('não vai dividir por zero')
        else:
            print(n1/n2)
    elif op == '5':
            break
    else:
        print('opção invalida')

 #############################################################
 #               METODO CORRETO DE ORGANIZAR                 #
 #############################################################

# Parte 1
### Definições de funções auxiliares

def soma(num1, num2):
    return num1 + num2

def diminuir(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):   
    if num2 != 0:
        return num1 / num2
    return 'Não divide por 0' 

# Definir a função principal - direcionar o fluxo da aplicação
def menu():
    while True: # adicionar um loop
        n1 = float(input('n1: '))
        n2 = float(input('n2: '))

        print('digite a aopção desejada:\n1- soma\n2- subtração\n3- multiplicação\n4- divisão\n5- sair')

        op = input('')

        if op == '1':
            print(soma(n1,n2))
        elif op == '2':
            print(diminuir(n1,n2))
        elif op == '3':
            print(multiplicar(n1,n2))
        elif op == '4':
            print(dividir(n1,n2))
        elif op == '5':
            break
        else:
            print('opção invalida')

# Diretiva para execução da função principal, diz para o interpretador onde o codigo esta.
if __name__ == '__main__':
    menu()

# Documentação do autor, nome, email, data

exit()

################################################################
# Como melhorar o codigo de if e elif com lambda e dicionarios #
################################################################

def soma(num1, num2):
    return num1 + num2

def diminuir(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):   
    if num2 != 0:
        return num1 / num2
    return 'Não divide por 0' 

def sair(*args):
    exit()

opcoes = {
    '1': soma,
    '2': diminuir,
    '3': multiplicar,
    '4': dividir,
    '5': sair
}

def menu():
    while True:
        n1 = float(input('n1: '))
        n2 = float(input('n2: '))

        print('digite a aopção desejada:\n1- soma\n2- subtração\n3- multiplicação\n4- divisão\n5- sair')

        op = input('')

        if op in opcoes.keys():
            print(opcoes[op](n1,n2))
        else:
            print('opção invalida')

if __name__ == '__main__':
    menu()

exit()

######################################################################
#                          FUNÇÃO LAMBDA                             #
######################################################################

opcoes = {
    '1': lambda x,y : x+y,
    '2': lambda x,y : x-y,
    '3': lambda x,y : x*y,
    '4': lambda x,y : x/y,
    '5': lambda x,y : exit()
}

def menu():
    while True:
        n1 = float(input('n1: '))
        n2 = float(input('n2: '))

        print('digite a aopção desejada:\n1- soma\n2- subtração\n3- multiplicação\n4- divisão\n5- sair')

        op = input('')

        if op in opcoes.keys():
            print(opcoes[op](n1,n2))
        else:
            print('opção invalida')

if __name__ == '__main__':
    menu()

exit()