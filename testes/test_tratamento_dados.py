from unittest import TestCase
from tratar_dados.tratamento_dados_cadastro import \
    tratar_cnpj
from tratar_dados.erro_tratamento import ErroTratamento
    
class TestTratarCNPJ(TestCase):
    def setUp(self):
        pass

    def testar_cpf_falha_string(self):
        cpf = 'asdasdas'

        self.assertRaises(tratar_cnpj(cpf), ErroTratamento)
    
    
        