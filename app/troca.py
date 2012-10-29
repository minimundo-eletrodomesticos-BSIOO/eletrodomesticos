#-*-coding:utf-8-*-
#Classe responsavel pela Troca de produtos que estejam na garantia

from datetime import *
from cliente import Cliente
from produto import Produto
from venda import Venda

class Troca(object):
	lista_troca = []
	registro_de_trocados =[]
	Venda.lista_vendas_1
	Venda.lista_vendas_2
	def __init__(self,data_via_string, defeito, nome_cliente_q_trocou ,nome_cliente_q_comprou, endereco_cli,descricao_prod,marca_prod, modelo_prod, numero_serie):
		self.data_da_troca = date(int(data_via_string[6:10]),int(data_via_string[3:5]),int(data_via_string[0:2]))
		self.defeito = defeito
		self.nome_cliente_q_trocou = nome_cliente_q_trocou
		self.nome_cliente_q_comprou = nome_cliente_q_comprou
		self.endereco_cli = endereco_cli
		self.marca_prod = marca_prod
		self.modelo_prod = modelo_prod
		self.numero_serie = numero_serie
		
		Troca._registro_de_troca(self)
		
	@classmethod
	def _registro_de_troca(self, registro):
		Troca.lista_troca.append(registro)
	
	
	def fazer_uma_troca(self):
		data_str = self.data_da_troca.strftime("%d/%m/%Y")
		for venda in range(len(Venda.lista_vendas_1)):
			if self.marca_prod == Venda.lista_vendas_1[venda].marca_prod:
				if Venda.lista_vendas_1[venda].consultar_garantia(data_str) == "Ainda está na garantia!":
					if Produto.estoque[venda].modelo == self.modelo_prod:
						Troca.registro_de_trocados.append(Produto.estoque[venda].numeros_de_serie[-1])
						produto = str(Produto.estoque[venda].numeros_de_serie[-1])
						Produto.estoque[venda].numeros_de_serie.remove(produto)
						return "Produto Trocado"
					else:
						return "Modelo imcompativel"
				else:
					 return "Garantia acabou"
			else:
				return "Produto não encontrado"
