#-*-coding:utf-8-*-
class Produtos(object):
	estoque = []
	numeros_de_serie = None
	def __init__(self,descricao ,marca, modelo,  quantidade):
		self.descricao = descricao
		self.marca = marca
		self.modelo = modelo
		self.quantidade = quantidade

		Produtos._armazena_aparelhos(self)

	@classmethod
	def _armazena_aparelhos(cls, itens):
		Produtos.estoque.append(itens)

	@staticmethod
	def inserir_numeros_de_serie(self, lista_de_numeros=[]):
		if self.quantidade < len(lista_de_numeros) or self.quantidade > len(lista_de_numeros):
			return "Quantidade acima ou abaixo do permitido o permitido eh = %d"%self.quantidade
		else:
			self.numeros_de_serie = lista_de_numeros


	def consultar_produto(self):
		return (self.descricao, self.marca, self.modelo, self.quantidade)
	
	@staticmethod
	def disponibilidade(self):
		disponibilidade = ""
		for indice in range(len(Produtos.estoque)):
			if Produtos.estoque[indice].quantidade > 0:
				disponibilidade = ("Quantidade em estoque = %i"%Produto.estoque[indice].quantidade)
			else:
				disponibilidade = ("Não há mais produtos desse produto em estoque")
		return disponibilidade
