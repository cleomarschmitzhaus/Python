#!/usr/bin/python3

# importação de modulos de outro "arquivo.py"

import modulo
#from modulo import PI, saudação

def soma(*args):
    soma = 0
    for num in args:
        soma += num
    return soma

print(modulo.PI)
print(modulo.saudacao())
print(soma(1,2,3,4))
print(modulo.soma(1,2))
print(__name__) # __main__
print(modulo.__name__)

# if __name__ =='__main__':
#     print(soma(1,2,3,4))

exit()

