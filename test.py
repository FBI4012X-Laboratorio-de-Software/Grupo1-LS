from unittest import TestCase
import unittest
from tratar_dados.tratamento_dados_cadastro import \
    tratar_cnpj, tratar_nivel
from tratar_dados.load_niveis import load_niveis_data
from tratar_dados.erro_tratamento import ErroTratamento
from tratar_dados.serializacao.distribuidor_DAO import DistribuidorDAO
from estrutura_dados.distrbuidor import Distribuidor


class TestTratarCNPJ(TestCase):
    def setUp(self):
        pass

    @unittest.expectedFailure
    def test_cpf_falha_string(self):
        cpf = 'asdasdas'
        tratar_cnpj(cpf)

    def test_cpf_sucesso(self):
        cpf = '52126507000190'
        tratar_cnpj(cpf)

    @unittest.expectedFailure
    def test_maior_erro(self):
        cpf = '290549995001333'
        tratar_cnpj(cpf)

    @unittest.expectedFailure
    def test_menor_erro(self):
        cpf = '2905499951333'
        tratar_cnpj(cpf)


class TestTratarClasse(TestCase):
    def setUp(self):
        pass

    def test_non_existent_class(self):
        tratar_nivel('DISTRIBUIDOR')

    def test_load_niveis(self):
        a = DistribuidorDAO()
        b = a.load_data()
        for c in b:
            print(str(c))

if __name__ == '__main__':
    unittest.main()
