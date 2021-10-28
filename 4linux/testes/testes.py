#!/usr/bin/python3

from random import randint
import unittest
import calculadora

class TesteCalculadora(unittest.TestCase):
    def test_soma(self):
        n1 = randint(0,999)
        n2 = randint(0,999)
        soma = n1 + n2
        self.assertEqual(soma, calculadora.soma(n1,n2))

    def test_divisao_esperada(self):
        n1 = randint(0,999)
        n2 = randint(1,999)
        div = n1 / n2
        self.assertEqual(div, calculadora.divisao(n1,n2))

    def test_divisao_por_zero(self):
        n1 = randint(0,999)
        n2 = 0
        div_zero = 'Não dividiras por zero'
        self.assertEqual(div_zero, calculadora.divisao(n1,n2))

exit()