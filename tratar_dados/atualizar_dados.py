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

def atualizar_dsitribuidor (dist : Distribuidor, pecas):
    
    pecas = dist.get_pecas_vendidas() + pecas
    nivel = dist.get_nivel()
    n_dist_formados = dist.get_n_dist_formados()

    if pecas >= 192 and n_dist_formados >= 8:
        if nivel != 'Distribuidor Nato':
            nivel = 'Distribuidor Nato'

    elif pecas >= 144 and n_dist_formados >= 6:
        if nivel != 'Distribuidor de Carreira':
            nivel = 'Distribuidor de Carreira'

    elif pecas >= 96 and n_dist_formados >= 4:
        if nivel != 'Distribuidor Sênior':
            nivel = 'Distribuidor Sênior'

    elif pecas >= 48 and n_dist_formados >= 2:
        if nivel != 'Distribuidor Líder':
            nivel = 'Distribuidor Líder'

    elif pecas >= 16:
        if nivel != 'Distribuidor':
            nivel = 'Distribuidor'
    
    dist.set_pecas_vendidas(pecas)
    dist.set_nivel(nivel)

    return dist
