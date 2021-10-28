#!/usr/bin/python3

# Abstração:
# simplificar o codigo escondendo algumas camadas
# Abstrair a complexidade de codigo

# Classes:
# Objetos a serem empilhados (Lugar para empilhar)-> Sempre tira o ultimo elemento, para evitar de quebrar -> atributo
# O ultimo elemento da pilha é o primeiro a sair -> metodos = comportamento


# pode criar varios objetos com a classe pilha
from _typeshed import Self
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
        def desempilhar(self):
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

## Herença permite reutilizar codigo

class colaborador:
    def __init__(self):
        self.nome = ''
        self.endereco = ''
        self.idade = 0
        self.salario = 0.0

    def apresentaColaborador(self):
        return f'Colabotrador: {self.nome}\n' \
                f'endereco: {self.endereco}\n' \
                f'idade: {self.idade}'


# para carregaer a herança de classe
class Gerente(colaborador):
    def calculaSalario(self, bonus):
        return self.salario * bonus

##############################################

## Para ganhar herança de mais de uma classe

class Mae:
    def __init__(self):
        self.nome = ''
        self.nacionalidade = 'Francesa'

    def falarFrances(self):
        return 'Bonjur'

class Pai:
    def __init__(self):
        self.nome = ''
        self.nacionalidade = 'Inglesa'
    
    def falarIngles(self):
        return 'Good Afternoon'

class Filha(Mae, Pai):
    pass

exit()

################################################################

## Polimorfismo
## é uma forma de mudar o comportamento de um metodo

class Mago:
    def __init__(self):
        self.clase ='Mago'
        self.habilidade = 'magia'

    def atacar(Self):
        return 'Ataque com magia'

class Soldado(Mago):
    def __init__(self):
        self.clase ='Soldado'
        self.habilidade = 'Uso de espada'

    def atacar(Self):
        return 'Ataque com espada'

class Arqueiro:
    def __init__(self):
        self.clase ='Arqueiro'
        self.habilidade = 'Uso de arco e flechas'

    def atacar(Self):
        return 'Ataque em distancia com arco e flexa'

exit()

############
## Com sistema de heranças

class profissao:
    def __init__(self):
        self.classe = ''
        self.habilidade = ''

class Mago(profissao):
    def atacar(self):
        return 'Ataque com magia'

class Soldado(profissao):
    def atacar(self):
        return 'Ataque com espada'

class Arqueiro(profissao):
    def atacar(self):
        return 'Ataque em distancia com arco e flexa'

#################################################################
## Composição de classe
## Clientes -> produtos {nome, preço, sku} <-> carinho {adicionar item, remover item}

#class produto:
    #def __init__(self,
        #sku ='',
        #nome ='',
        #desc = '',
        #preco = 0.0
    #):

    #self.sku = sku
    #self.nome = nome
    #self.desc = desc
    #self.preco = preco

exit()

class carrinhoDeCompras:
    def __init__(self):
        self.carrinho = []
        self.quantidade_produtos = 0
        self.total = 0

    def adicionarProduto(self, produto):
        self.carrinho.append(produto)
        self.quantidade_produtos += 1

    def removerProduto(self, nome_produto):

        for produto in self.carrinhos:
            if produto.nome == nome_produto:
                self.carrinho.remove(produto)
                removido = True
                return 'O produto foi removido do carrinho'

exit()

