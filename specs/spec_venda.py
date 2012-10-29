#-*-coding:utf-8-*-
import sys
from datetime import *

sys.path.append('../app/')

import unittest
from should_dsl import should
from produto import Produto
from venda import Venda
from cliente import Cliente

class Test_Venda_Spec(unittest.TestCase):
	def setUp(self):
		self.cliente = Cliente("Ela", "Casa dela")
		self.produto = Produto('Samsung Galaxy', 'SAMSUNG', 'I8150', 3)
		self.produto.inserir_numeros_de_serie(["HWWx3", "HXD#F","LKJ#2"])
	
	def test_vender_aparelho(self):
		venda = Venda("Ela", "Casa dela","Samsung Galaxy", "SAMSUNG", "I8150", "26/10/2012")
		self.produto.estoque[0].numeros_de_serie[0] |should| equal_to("HWWx3")
		venda.fazer_venda() 

		venda.nome_cli |should| equal_to("Ela")
		venda.lista_vendas_2[0] |should| equal_to("LKJ#2")
		venda.lista_vendas_1[0].marca_prod |should| equal_to("SAMSUNG")

	def test_impossivel_vender_produto_so_tem_no_mostruario(self):
		venda = Venda("Ela", "Casa dela","Samsung Galaxy", "SAMSUNG", "I8150", "26/10/2012")
		venda.fazer_venda()
		venda.fazer_venda() 
		venda.fazer_venda() |should| equal_to("impossivel vender")
	
	def test_esta_na_garantia(self):
		self.venda = Venda("Ela", "Casa dela","Samsung Galaxy", "SAMSUNG", "I8150", "26/10/2012")
		self.venda.fazer_venda()
		self.venda.lista_vendas_1[0].nome_cli |should| equal_to("Ela")
		self.venda.lista_vendas_1[0].descricao_prod |should| equal_to('Samsung Galaxy')
		self.venda.consultar_garantia("26/10/2012") |should| equal_to("Ainda está na garantia!")

	def test_esta_fora_da_garantia(self):
		self.venda = Venda("Ela", "Casa dela","Samsung Galaxy", "SAMSUNG", "I8150", "26/10/2012")
		self.venda.fazer_venda()
		self.venda.consultar_garantia("26/10/2016") |should| equal_to("Esta fora da garantia")




if __name__ == "__main__":
    unittest.main()
