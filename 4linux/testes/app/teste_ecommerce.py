import unittest
from ecommerce import Produto, CarrinhoDeCompras

class TesteEcommerce(unittest.TestCase):
    def setUp(self): # preparação do experimento
        self.p1 = Produto('camiseta', 9.90)
        self.p2 = Produto('Calça Jeans', 10.90)
        self.c1 = CarrinhoDeCompras()
    
    def adiciona_produtos_no_carrinho(self): # ação 1 a ser tomada
        self.c1.adicionaProduto(self.p1)
        self.c1.adicionaProduto(self.p2)

    def calcula_total_de_compras(self): # ação 2 ...
        self.total_de_compras = self.c1.calculaTotalDeCompras()

    def make_assertions(self): # Checagem dos resultados
        self.assertEqual(2, len(self.c1.carrinho))
        self.assertEqual(self.p1.preco+self.p2.preco, self.total_de_compras)

    def teste_ecommerce(self): # executa passo a passo e valida o teste
        self.adiciona_produtos_no_carrinho()
        self.calcula_total_de_compras()
        self.make_assertions()

exit()