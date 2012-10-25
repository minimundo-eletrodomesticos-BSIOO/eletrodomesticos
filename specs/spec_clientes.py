import sys
sys.path.append('./app')
import unittest
from should_dsl import should
from cliente import Clientes

class Test_Cliente_Spec(unittest.TestCase):
	def setUp(self):
		self.cliente = Clientes("Tu", "Tua Residencia")
		
	def test_verifica_registro_cliente(self):
		self.cliente.consulta_clientes() |should| equal_to(("Tu", "Tua Residencia"))


if __name__ ==  "__main__":
	unittest.main() 
