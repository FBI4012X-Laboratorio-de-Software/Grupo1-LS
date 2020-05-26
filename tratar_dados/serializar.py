import pickle
import os
from typing import List, Tuple
from configparser import RawConfigParser
from estrutura_dados.distrbuidor import Distribuidor
from estrutura_dados.vendas import Vendas


def serializar(dados_vendas, dados_dist) -> Tuple[List[Vendas], List[Distribuidor]]:

    config = RawConfigParser()
    config.read('.config.cfg')

    vendas_save_file_path = config.get('serializacao', 'vendas_path')
    dist_save_file_path = config.get('serializacao', 'dist_path')

    dump_data_list(vendas_save_file_path, dados_vendas)
    dump_data_list(dist_save_file_path, dados_dist)


def dump_data_list(load_path: str, obj_list: list) -> None:

    if os.path.exists(load_path):
        with open(load_path, 'wb') as load_file:
            try:
                pickle.dump(obj_list, load_file)
            except Exception as e:
                print(f'bota um log aqui pelamor de deus\n{e}')
