from typing import List, Tuple
import logging
from estrutura_dados.distrbuidor import Distribuidor
from estrutura_dados.vendas import Vendas
from tratar_dados.serializar import serializar
from tratar_dados.puxar_dados import puxar_dados
from datetime import date


def atualizar_dados(
    dados_vendas: List[Vendas],
    dados_dist: List[Distribuidor],
) -> Tuple[List[Vendas], List[Distribuidor]]:

    serializar(dados_vendas, dados_dist)
    dados_atualizados = puxar_dados()

    return dados_atualizados

def atualizar_distribuidor (dist : Distribuidor, pecas):
    
    pecas = dist.get_pecas_vendidas() + pecas
    nivel = dist.get_nivel()
    n_dist_formados = dist.get_n_dist_formados()

    logging.info('Distribuidor ' + dist.get_dist_nome + ' foi atualizado.')
    logging.info(' >Total de pecas vendidas: ' + pecas)
    logging.info(' >Nivel:                   ' + nivel)
    logging.info(' >Distribuidores formados: ' + n_dist_formados)

    if pecas >= 192 and n_dist_formados >= 8:
        if nivel != 'Distribuidor Nato':
            nivel = 'Distribuidor Nato'
            logging.info(dist.get_dist_nome + ' virou um distribuidor Nato!')

    elif pecas >= 144 and n_dist_formados >= 6:
        if nivel != 'Distribuidor de Carreira':
            nivel = 'Distribuidor de Carreira'
            logging.info(dist.get_dist_nome + ' virou um distribuidor de Carreira!')

    elif pecas >= 96 and n_dist_formados >= 4:
        if nivel != 'Distribuidor Sênior':
            nivel = 'Distribuidor Sênior'
            logging.info(dist.get_dist_nome + ' virou um distribuidor Senior!')

    elif pecas >= 48 and n_dist_formados >= 2:
        if nivel != 'Distribuidor Líder':
            nivel = 'Distribuidor Líder'
            logging.info(dist.get_dist_nome + ' virou um distribuidor Lider!')

    elif pecas >= 16:
        if nivel != 'Distribuidor':
            nivel = 'Distribuidor'
            logging.info(dist.get_dist_nome + ' virou um distribuidor!')
    
    dist.set_pecas_vendidas(pecas)
    dist.set_nivel(nivel)

    dist.set_last_update(date.today())

    return dist
