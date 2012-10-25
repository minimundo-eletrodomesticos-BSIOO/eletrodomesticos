#-*-coding:utf-8-*-
class Produtos(object):
	estoque = []
	numeros_de_serie = []
	def __init__(self,descricao ,marca, modelo,  quantidade):
		self.descricao = descricao
		self.marca = marca
		self.modelo = modelo
		self.quantidade = quantidade

		Produtos._armazena_aparelhos(self)

	@classmethod
	def _armazena_aparelhos(cls, itens):
		Produtos.estoque.append(itens)

	def inserir_numeros_de_serie(self, lista_de_numeros=[]):
		if self.quantidade < len(lista_de_numeros) or self.quantidade > len(lista_de_numeros) :
			return "Quantidade acima ou abaixo do permitido"
		else:
			self.numeros_de_serie = lista_de_numeros


	def consultar_produto(self):
		return (self.descricao, self.marca, self.modelo, self.quantidade)
	
	#@staticmethod
	def total_de_aparelhos_disponiveis(self):
		total_de_aparelhos = 0
		for x in range(len(Produtos.estoque)):
			if Produtos.estoque[x].quantidade > 0:
				total_de_aparelhos += self.estoque[x].quantidade
		return total_de_aparelhos
