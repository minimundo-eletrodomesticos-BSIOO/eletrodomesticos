#-*-coding:utf-8-*-
import sys
import unittest

sys.path.append('../app/')


from should_dsl import should
from cliente import Cliente

class Test_Cliente_Spec(unittest.TestCase):
	def test_cria_cliente(self):
		self.cliente = Cliente("Ela", "Casa dela")
		
	def test_verifica_registro_cliente(self):
		self.cliente.consulta_clientes() |should| equal_to(("Ela", "Casa dela"))


if __name__ ==  "__main__":
	unittest.main() 
