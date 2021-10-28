#!/usr/bin/python3

### Tratamento de Exeções e teste Unitário

### iniciar em 7.2 exeções
## exeção é quandop seu programa pode travar

dic = {
    '1': lambda x,y : x + y,
    '2': lambda x,y : x - y,
    '3': lambda x,y : x * y,
    '4': lambda x,y : x / y,
    '5': lambda x,y : exit()
}

while True:
    
    # Na tentativa de dividir por 0 vai dar erro
    # Digitar uma chave que não existe
    # tratamento de erro

    try: # bloco com possivel erro

        n1 = float(input('N1: '))
        n2 = float(input('N2: '))

        op = input(f'Digite a opção desejada \n' \
                    f'1 - Soma \n' \
                    f'2 - Subtração \n' \
                    f'3 - Multiplicação \n' \
                    f'4 - Divisão \n' \
                    f'5 - Sair \n')
    # quanto mais erros previstos melhor
        res =  dic[op](n1,n2)
    except ZeroDivisionError:
        print('Não pode dividir por zero')
    except KeyError:
        print('Digite uma opção valida')
    except ValueError:
        print('Digite somente numeros')
    except Exception as err: # para erros desconhecidos não previstos
        print('Erro desconhecido', err)
    else: # não é obrigatório
        # proxima instrução caso for bem sucedido
        print(res)
    finally: # não é obrigatório
        print('Passei por aqui')

exit()

