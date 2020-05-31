import os
import pickle
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
                    print(f'bota um log aqui pelamor de deus\n{e}')

        return lista_objeto

    def save_data(self, obj_list):
        file_path = self.config.get('serializacao', 'dist_path')

        if os.path.exists(file_path):
            with open(file_path, 'wb') as load_file:
                try:
                    pickle.dump(obj_list, load_file)
                except Exception as e:
                    print(f'bota um log aqui pelamor de deus\n{e}')

    def update_data(self, obj_list):
        self.save_data(obj_list)
        return self.load_data()
