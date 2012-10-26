#-*-coding:utf-8-*-
import sys
import unittest
from should_dsl import should
sys.path.append('app')
from produto import Produto
from venda import Venda
from cliente import Cliente
from troca import Troca

class Test_Trocar_Spec(unittest.TestCase):
	def setUp(self):
		self.cliente = Cliente("Tu", "Tua Residencia")
		self.produto = Produto('Samsung Galaxy', 'SAMSUNG', 'I8150', 5)
		self.produto.inserir_numeros_de_serie(["HWWx3", "HXD#F","LKJ#2","LKJ#3","L45#2"])
		self.venda = Venda("Tu", "Tua Residencia",'Samsung Galaxy', 'SAMSUNG', 'I8150')
		self.troca1 = Troca("26/11/2015", "Não liga","Tu", "Tua Residencia",'Samsung Galaxy', 'SAMSUNG', 'I8150','LKJ#2' )
		self.troca2 = Troca("26/11/2012","Não liga","Tu", "Tua Residencia",'Samsung Galaxy', 'SAMSUNG', 'I8150','HXD#F' )
		
	
	def test_trocar_produto(self):
		self.venda.fazer_venda(2)
		self.venda.lista_vendas_2[0] |should| equal_to('HXD#F')
		self.venda.lista_vendas_2[1] |should| equal_to('LKJ#2')
		self.troca1.fazer_uma_troca()
		
		self.troca1.lista_troca[0].nome_cli |should| equal_to("Tu")
		self.troca1.registro_de_trocados[0] |should| equal_to("L45#2")
		
	def test_trocar_nao_passou(self):
		self.troca = Troca("26/11/2015", "Não liga","Tu", "Tua Residencia",'Samsung Galaxy', 'LG', 'I8150','LKJ#2' )
		self.troca.fazer_uma_troca() |should| equal_to("Produto não encontrado")
		
		#troca.registro_de_trocados[1] |should| equal_to('HWWx3')
	
	

if __name__ == "__main__":
    unittest.main()
