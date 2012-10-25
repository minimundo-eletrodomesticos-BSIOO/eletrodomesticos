#-*-coding:utf-8
class Clientes(object):
	relacao_clientes = []
	def __init__(self,nome, endereco):
		self.nome = nome
		self.endereco = endereco
		Clientes.insert_clientes(self)
		

	@classmethod
	def insert_clientes(cls, relacao_clientes):
		Clientes.relacao_clientes.append(relacao_clientes)
		
		
	def consulta_clientes(self):
		return (self.nome, self.endereco)