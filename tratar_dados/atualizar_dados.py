from typing import List, Tuple
from estrutura_dados.distrbuidor import Distribuidor
from estrutura_dados.vendas import Vendas
from tratar_dados.serializar import serializar
from tratar_dados.puxar_dados import puxar_dados


def atualizar_dados(
    dados_vendas: List[Vendas],
    dados_dist: List[Distribuidor],
) -> Tuple[List[Vendas], List[Distribuidor]]:

    serializar(dados_vendas, dados_dist)
    dados_atualizados = puxar_dados()

    return dados_atualizados
