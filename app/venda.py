#-*-coding:utf-8-*-
from datetime import *
from cliente import Clientes
from produto import Produtos

class Vendas(Clientes, Produtos):
	relatorio_de_vendas = []
	def __init__(self,nome_cli, endereco_cli,descricao_prod,marca_prod, modelo_prod, quantidade_prod, n_serie_prod):
		Clientes.__init__(self, nome_cli, endereco_cli)
		Produtos.__init__(self, descricao_prod,marca_prod, modelo_prod, quantidade_prod, n_serie_prod)
		self.data_da_compra = date.today()
		Vendas._salvar_vendas(self)
			
	@classmethod
	def _salvar_vendas(cls, conteudo):
		Vendas.relatorio_de_vendas.append(conteudo)
	
	def consultar_garantia(self):
		ano_garantia = date.today().year + 1
		data_garantia = date(ano_garantia, self.data_da_compra.month, self.data_da_compra.day)
		if date.today() <= data_garantia:
			return "Ainda está na garantia!"
		else:
			return "Está fora da garantia"