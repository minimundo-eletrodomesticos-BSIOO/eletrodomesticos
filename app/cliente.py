#-*-coding:utf-8-*-
#Classe responsavel pela organização dos clientes
class Cliente(object):
	relacao_clientes = []
	def __init__(self,nome, endereco):
		self.nome = nome
		self.endereco = endereco
		self.cliente_estrela? = True
		Cliente.insert_clientes(self)
		

	@classmethod
	def insert_clientes(cls, relacao_clientes):
		Cliente.relacao_clientes.append(relacao_clientes)
		
		
	def consulta_clientes(self):
		return (self.nome, self.endereco)
		
	@classmethod
	def clientes_com_sorte(cls):
		registro = ""
		for indice in range(len(Cliente.relacao_clientes)):
			if Cliente.relacao_clientes[indice].cliente_estrela? == True:
				registro += "Nome: "+Cliente.relacao_clientes[indice].nome+"\nEndereco: "+Cliente.relacao_clientes[indice].endereco+"\n"
				return registro
