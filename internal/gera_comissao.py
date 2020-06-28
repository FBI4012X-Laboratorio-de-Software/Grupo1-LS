import pandas as pd
import os
from configparser import RawConfigParser
from typing import DefaultDict, List, Union, Tuple
from datetime import date, datetime
from internal.get_filhos import name_compare_com_nivel
from estrutura_dados.distrbuidor import Distribuidor
import math


def gera_comissao(name: str, sd: datetime, ed: datetime) -> Union[str, float]:
    name = name.upper()
    le_dict = get_data()
    
    valor_comissao: float = 0
    pecas_a_adicionar: float = 0

    filhos_list: List[(Distribuidor, int)] = name_compare_com_nivel(name.upper())

    filhos_list[0][0].get_porcentagen_vendas()
    if name in le_dict.keys() and isinstance(filhos_list, list):
        filhos_list: List[Distribuidor] = name_compare_com_nivel(name)
        comissao_ini = 0

        for dist, filho_num in filhos_list:

            lista_valores = dist.get_porcentagem_filhos()

            desconto, comissao, lucro = dist.get_porcentagen_vendas()

            if dist.get_dist_nome() in le_dict.keys():

                values = le_dict[dist.get_dist_nome()]

                for val in values:
                    if val[0] >= sd.date() and val[0] < ed.date():

                        if math.isnan(comissao):

                            if filho_num == 0:
                                comissao_ini += val[2] * lucro
                            else:
                                comissao_ini += val[2] * lucro * float(lista_valores[filho_num - 1])
                        else:
                            if filho_num == 0:
                                comissao_ini += val[2] * comissao
                            else:
                                comissao_ini += val[2] * comissao * float(lista_valores[filho_num - 1])
        return float(comissao_ini)
    else:
        return 'Nome Não Encontrado'

def get_data() -> dict:
    config = RawConfigParser()
    config.read('.config.cfg')
    file_list = config['comissoes']['comissoes_path'].split(',')
    nomes_vend = []
    data_pedidos = []
    real_valor_pecas = []
    valor_a_pagar = []

    for file in file_list:
        valor_pecas = []
        planilha = pd.read_excel(file, header=6)
        nomes_vend.extend(list(planilha['VENDEDOR'].dropna()))
        data_pedidos.extend(list(planilha['DATA PEDIDO'].dropna()))
        valor_pecas.append(list(planilha['VALOR PEÇA'].dropna()))
        valor_a_pagar.extend(list(planilha['VALOR'].dropna()))
        for i in valor_pecas[0]:
            if i != ' ':
                real_valor_pecas.append(i)

    le_dict: DefaultDict[str, list] = DefaultDict(list)

    for (nome, data, peca, valor) in zip(nomes_vend, data_pedidos, real_valor_pecas, valor_a_pagar):

        le_dict[nome.upper()].append((data.date(), peca, round(valor, 2)))

    return le_dict


if __name__ == "__main__":
    gera_comissao()
