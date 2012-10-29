#-*-coding:utf-8-*-
#Classe responsavel pela Geração de Vendas

from datetime import *
from cliente import Cliente
from produto import Produto

class Venda(object):
	lista_vendas_1 = []
	lista_vendas_2 = []
	Produto.estoque
	def __init__(self,nome_cli, endereco_cli,descricao_prod,marca_prod, modelo_prod,
data_via_string):
		self.nome_cli = nome_cli
		self.endereco_cli = endereco_cli
		self.descricao_prod = descricao_prod
		self.marca_prod = marca_prod
		self.modelo_prod = modelo_prod
		self.data_da_compra = date.today()
		Venda._salvar_vendas(self)
			
	@classmethod
	def _salvar_vendas(cls, conteudo):
		Venda.lista_vendas_1.append(conteudo)

	def consultar_garantia(self, data_object):
		ano_garantia = self.data_da_compra.year + 1
		data_garantia = date(ano_garantia, self.data_da_compra.month, self.data_da_compra.day)
		data_object = date(int(data_object[6:10]),int(data_object[3:5]),int(data_object[0:2]))
		if data_object <= data_garantia:
			return "Ainda está na garantia!"
		else:
			return "Esta fora da garantia"
	
	def fazer_venda(self):
		for indice in range(len(Produto.estoque)):
			if Produto.estoque[indice].marca == self.marca_prod:
				if len(Produto.estoque[indice].numeros_de_serie) > 1:
					self.lista_vendas_2.append(Produto.estoque[indice].numeros_de_serie[-1])
					produto = str(Produto.estoque[indice].numeros_de_serie[-1])
					Produto.estoque[indice].numeros_de_serie.remove(produto)
				else:
					return "impossivel vender"
	
		