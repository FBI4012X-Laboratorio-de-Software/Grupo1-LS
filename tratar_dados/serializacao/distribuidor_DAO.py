import os
import pickle
import logging
from tratar_dados.serializacao.DAO import DAO


class DistribuidorDAO(DAO):
    def __init__(self):
        super().__init__()

    def load_data(self):
        file_path = self.config.get('serializacao', 'dist_path')

        lista_objeto = []

        if os.path.exists(file_path):
            with open(file_path, 'rb') as load_file:
                try:
                    lista_objeto = pickle.load(load_file)
                except Exception as e:
                    logging.warning('Erro ao carregar arquivo de distribuidor: ' + str(e))
        else:
            logging.error('Erro ao carregar arquivo de distribuidor: caminho ' + file_path + ' nao existe')    

        logging.debug('Arquivo de distribuidor carregado.')

        return lista_objeto

    def save_data(self, obj_list):

        lista_objeto = self.load_data()
        file_path = self.config.get('serializacao', 'dist_path')
        lista_objeto.append(obj_list)

        if os.path.exists(file_path):
            with open(file_path, 'wb') as load_file:
                try:
                    pickle.dump(lista_objeto, load_file)
                except Exception as e:
                    logging.warning('Erro ao salvar arquivo de distribuidor: ' + str(e))
        else:
            logging.error('Erro ao salvar arquivo de distribuidor: caminho ' + file_path + ' nao existe')   

        logging.debug('Arquivo de distribuidor salvo.')

    def update_data(self, obj_list):
        self.save_data(obj_list)
        return self.load_data()
