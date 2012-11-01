#-*-coding:utf-8-*-
#Classe responsavel pela organização dos clientes
class Cliente(object):
	relacao_clientes = []
	def __init__(self,nome, endereco):
		self.nome = nome
		self.endereco = endereco
		self.cliente_estrela = True
		Cliente.insert_clientes(self)
		

	@classmethod
	def insert_clientes(cls, relacao_clientes):
		Cliente.relacao_clientes.append(relacao_clientes)
		
		
	def consulta_clientes(self):
		return (self.nome, self.endereco)
		
	@classmethod
	def clientes_com_sorte(self):
		estrelas = ""
		for estrela in Cliente.relacao_clientes:
			if estrela.cliente_estrela == True:
				estrelas += ("Nome.: "+estrela.nome+"\nEnd.: "+estrela.endereco)
		return  estrelas
