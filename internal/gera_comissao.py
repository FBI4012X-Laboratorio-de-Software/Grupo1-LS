import pandas as pd
import os
from configparser import RawConfigParser
from typing import DefaultDict
from datetime import date


def gera_comissao():

    le_dict = get_data()
    print(le_dict)


def get_data():
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

        le_dict[nome].append((data.date(), peca, valor))

    return le_dict


if __name__ == "__main__":
    gera_comissao()
