#-*-coding:utf-8-*-
from datetime import *
from cliente import Cliente
from produto import Produto

class Venda(object):
	lista_vendas_1 = []
	lista_vendas_2 = []
	Produto.estoque
	def __init__(self,nome_cli, endereco_cli,descricao_prod,marca_prod, modelo_prod):
		self.nome_cli = nome_cli
		self.endereco_cli = endereco_cli
		self.data_da_compra = date.today()
		self.descricao_prod = descricao_prod
		self.marca_prod = marca_prod
		self.modelo_prod = modelo_prod
		Venda._salvar_vendas(self)
			
	@classmethod
	def _salvar_vendas(cls, conteudo):
		Venda.lista_vendas_1.append(conteudo)

	def consultar_venda(self):
		return produto.marca
	
	def consultar_garantia(self):
		ano_garantia = date.today().year + 1
		data_garantia = date(ano_garantia, self.data_da_compra.month, self.data_da_compra.day)
		if date.today() <= data_garantia:
			return "Ainda está na garantia!"
		else:
			return "Está fora da garantia"
	
	def fazer_venda(self,  quantidade):
		for indice in range(len(Produto.estoque)):
			if Produto.estoque[indice].marca == self.marca_prod:
				for x in range(quantidade):
					if len(Produto.estoque[indice].numeros_de_serie) >= 1:
						self.lista_vendas_2.append(Produto.estoque[indice].numeros_de_serie[quantidade-1])
						produto = str(Produto.estoque[indice].numeros_de_serie[quantidade-1])
						Produto.estoque[indice].numeros_de_serie.remove(produto)
					else:
						return "impossivel vender"	
