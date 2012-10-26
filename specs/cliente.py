#-*-coding:utf-8-*-

class Cliente(object):
	relacao_clientes = []
	def __init__(self,nome, endereco):
		self.nome = nome
		self.endereco = endereco
		Cliente.insert_clientes(self)
		

	@classmethod
	def insert_clientes(cls, relacao_clientes):
		Cliente.relacao_clientes.append(relacao_clientes)
		
		
	def consulta_clientes(self):
		return (self.nome, self.endereco)
