#!/usr/bin/python3

def soma(x,y):
        return x + y

def divisao(x,y):
    try:
        return x / y
    except ZeroDivisionError:
        return 'Não dividiras por zero'

exit()