#-*-coding:utf-8-*-
import sys

sys.path.append('../app/')

import unittest
from should_dsl import should
from datetime import *
from produto import Produto
from venda import Venda
from cliente import Cliente
from troca import Troca

class Test_Trocar_Spec(unittest.TestCase):
	def setUp(self):
		self.cliente_1 = Cliente("Tu", "Tua Residencia")
		self.cliente_2 = Cliente("Ela", "Residencia dela")
		self.produto = Produto('Samsung Galaxy', 'SAMSUNG', 'I8150', 5)
		self.produto.inserir_numeros_de_serie(["HWWx3", "HXD#F","LKJ#2","LKJ#3","L45#2"])
		self.venda = Venda("Tu", "Tua Residencia",'Samsung Galaxy', 'SAMSUNG', 'I8150', "29/10/2012")
		
		
	def test_trocar_produto(self):
		self.venda.fazer_venda()
		self.venda.fazer_venda()
		troca = Troca("29/10/2012", "Ela","Não liga","Tu", "Tua Residencia",'Samsung Galaxy', 'SAMSUNG', 'I8150','LKJ#2' )
		troca.fazer_uma_troca() |should| equal_to("Produto Trocado")
	
	def test_trocar_produto_nao_encontrado(self):
		troca = Troca("29/10/2012", "Ela","Não liga","Tu", "Tua Residencia",'Samsung Galaxy', 'LG', 'I8150','LKJ#2' )
		troca.fazer_uma_troca() |should| equal_to("Produto não encontrado")
	
	def test_trocar_produto_garantia_acabou(self):
		troca = Troca("29/10/2015", "Ela","Não liga","Tu", "Tua Residencia",'Samsung Galaxy', 'SAMSUNG', 'I8150','LKJ#2' )
		troca.fazer_uma_troca() |should| equal_to("Garantia acabou")

if __name__ == "__main__":
    unittest.main()
