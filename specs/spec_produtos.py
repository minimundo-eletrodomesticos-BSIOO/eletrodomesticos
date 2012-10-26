#-*-coding:utf-8-*-
import sys
import unittest
from should_dsl import should
sys.path.append('app')
from produto import Produto

class Test_Aparelho_Spec(unittest.TestCase):
	def test_criar_aparelho(self):
		produto = Produto('Samsung Galaxy W wonder', 'SAMSUNG', 'I8150', 3)

	def test_consultar_produto(self):
		produto = Produto('Samsung Galaxy W wonder', 'SAMSUNG', 'I8150', 3)
		produto.inserir_numeros_de_serie(["HWWx3", "HXD#F","LKJ#2"])
		produto.consultar_produto() |should| equal_to(('Samsung Galaxy W wonder', 'SAMSUNG',
'I8150', 3))

	def test_gerar_numero_de_serie_nao_deve_passar(self):
		produto = Produto('Samsung Galaxy W wonder', 'SAMSUNG', 'I8150', 3)
		produto.inserir_numeros_de_serie(["HWWx3", "HXD#F","LKJ#2", "4565"]) |should| equal_to("Quantidade acima ou abaixo do permitido")

	def test_consultar_total_de_produtos_disponiveis(self):
		produto_1 = Produto('Samsung Galaxy W wonder', 'SAMSUNG', 'I8150', 3)
		produto_2 = Produto('Samsung Galaxy SE', 'SAMSUNG', 'I9140', 4)
		produto_1.total_de_aparelhos_disponiveis() |should| equal_to(10)
		


if __name__ == "__main__":
    unittest.main()