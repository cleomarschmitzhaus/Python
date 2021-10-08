#!/usr/bin/python3

# Abstração:
# simplificar o codigo escondendo algumas camadas
# Abstrair a complexidade de codigo

# Classes:
# Objetos a serem empilhados (Lugar para empilhar)-> Sempre tira o ultimo elemento, para evitar de quebrar -> atributo
# O ultimo elemento da pilha é o primeiro a sair -> metodos = comportamento


# pode criar varios objetos com a classe pilha
from typing_extensions import TypeVarTuple


class Pilha:
    def __init__(self): # variáveis <> atributos
        self.Pilha = []
        self.topo = 0

# p = Pilha.topo
# p2 = Pilha.Pilha
# Outra_vez = Pilha

        # Comportamentos
        # add comportamento na pilha (empilhar)

        def empilhar(self, item): # self indoca que vc vai usar o proprio objeto # item = alguma coisa
            self.pilha.append(item)
            self.topo += 1    

        # remover elemento  da pilha (desempilhar)
        def desempilhar(self,):
            if not self.estaVazia():
                item_removido = self.pilha[-1]
                del self.pilha[-1]
                self.topo -= 1
                return f'o item {item_removido} da pilha'
            return 'Pilha esta vazia'

        # definir se a pilha esta vazia
        def estaVazia(self):
            if len(self.pilha) == 0:
                return True
            return False
        # return len(self.pilha) == 0

        # dander init é um construtor __init__ = criar os atributos
        # tambem carrega os metodos
        # aceita paremetros __init__(self, pilha=[], topo=0)
        # self.pilha referencia o objeto
        # para iniciar a pilha com valor dentro
        # p = pilha([0,1,2,3,4], len[0,1,2,3,4])

        # self = para ter acesso aos elementos do seu objeto
        # se tornara funções, comportamentos do objetos
        
exit()

######################################################################

# Encapsulamento
# serve para protejet a classe de manipulações
# trabalha com convenções

class A:
    def __init__(self):
        self.pilha = []
        self.topo=0
        self._uso_interno = True # so a classe pode usar
        self.__mangled = True # ninguem pode usar

exit()

####### proxima aula 7 herenças POO












