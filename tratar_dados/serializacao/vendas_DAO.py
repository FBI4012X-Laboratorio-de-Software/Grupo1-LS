import os
import pickle
import logging
from tratar_dados.serializacao.DAO import DAO


class VendasDAO(DAO):
    def __init__(self):
        super().__init__()

    def load_data(self):
        print(self.config)
        file_path = self.config.get('serializacao', 'vendas_path')

        lista_objeto = []

        if os.path.exists(file_path):
            with open(file_path, 'rb') as load_file:
                try:
                    lista_objeto = pickle.load(load_file)
                except Exception as e:
                    logging.error('Erro ao carregar arquivo de vendas: ' + e)
        else:
            logging.error('Erro ao carregar arquivo de vendas: caminho ' + file_path + ' nao existe')    

        return lista_objeto

    def save_data(self, obj_list):

        lista_objeto = self.load_data()
        lista_objeto.append(obj_list)

        file_path = self.config.get('serializacao', 'vendas_path')

        if os.path.exists(file_path):
            with open(file_path, 'wb') as load_file:
                try:
                    pickle.dump(lista_objeto, load_file)
                except Exception as e:
                    logging.error('Erro ao salvar arquivo de vendas: ' + e)
        else:
            logging.error('Erro ao salvar arquivo de vendas: caminho ' + file_path + ' nao existe')    

    def update_data(self, obj_list):
        self.save_data(obj_list)
        return self.load_data()