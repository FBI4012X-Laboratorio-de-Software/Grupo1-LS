from configparser import RawConfigParser
import os


class DAO(object):

    def __init__(self):
        config = RawConfigParser()
        config.read('.config.cfg')
        self.config = config

    def load_data(self):
        pass

    def save_data(self, obj_list):
        pass

    def update_data(self, obj_list):
        pass
