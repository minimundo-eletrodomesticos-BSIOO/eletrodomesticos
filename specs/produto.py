#-*-coding:utf-8-*-

class Produto(object):
	estoque = []
	numeros_de_serie = []
	def __init__(self,descricao ,marca, modelo,  quantidade):
		self.descricao = descricao
		self.marca = marca
		self.modelo = modelo
		self.quantidade = quantidade

		Produto._armazena_aparelhos(self)

	@classmethod
	def _armazena_aparelhos(cls, itens):
		Produto.estoque.append(itens)

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
		for x in range(len(Produto.estoque)):
			if Produto.estoque[x].quantidade > 0:
				total_de_aparelhos += self.estoque[x].quantidade
		return total_de_aparelhos
	
	def disponibilidade_do_aparelho(self, marca, modelo):
		qt_disponivel = 0
		for x in range(len(Produto.estoque)):
			if (Produto.estoque[x].marca == marca) and (Produto.estoque[x].modelo == modelo):
				qt_disponivel = self.estoque[x].quantidade
		return qt_disponivel
