#-*-coding:utf-8-*-
import sys
import unittest
from should_dsl import should
sys.path.append('app')
from cliente import Cliente

class Test_Cliente_Spec(unittest.TestCase):
	def setUp(self):
		self.cliente = Cliente("Tu", "Tua Residencia")
		
	def test_verifica_registro_cliente(self):
		self.cliente.consulta_clientes() |should| equal_to(("Tu", "Tua Residencia"))


if __name__ ==  "__main__":
	unittest.main() 
