#-*-coding:utf-8-*-
import sys

sys.path.append('../app/')

import unittest
from should_dsl import should
from produto import Produto
from venda import Venda
from cliente import Cliente

class Test_Venda_Spec(unittest.TestCase):
	def setUp(self):
		self.cliente = Cliente("Tu", "Tua Residencia")
		self.produto = Produto('Samsung Galaxy', 'SAMSUNG', 'I8150', 3)
		self.produto.inserir_numeros_de_serie(["HWWx3", "HXD#F","LKJ#2"])
	
	def test_vender_aparelho(self):
		venda = Venda(self.cliente.nome, self.cliente.endereco,self.produto.descricao, self.produto.marca, self.produto.modelo)
		self.produto.estoque[0].numeros_de_serie[0] |should| equal_to("HWWx3")
		venda.fazer_venda(2) 

		venda.nome_cli |should| equal_to("Tu")
		venda.lista_vendas_2[0] |should| equal_to("HXD#F")
		venda.lista_vendas_1[0].marca_prod |should| equal_to("SAMSUNG")
	
	def test_verificar_se_esta_na_garantia(self):
		venda = Venda(self.cliente.nome, self.cliente.endereco,self.produto.descricao, self.produto.marca, self.produto.modelo)
		venda.fazer_venda(1) 
		venda.lista_vendas_1[0].nome_cli |should| equal_to("Tu")
		venda.lista_vendas_1[0].descricao_prod |should| equal_to('Samsung Galaxy')
		venda.consultar_garantia() |should| equal_to("Ainda está na garantia!")


if __name__ == "__main__":
    unittest.main()
