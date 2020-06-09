from datetime import date

class Distribuidor(object):
    def __init__(self, *args) -> None:
        """id , nome, cnpj, contato, nivel, nome_pai, pecas_vendidas, last_up(date)"""

        self._dist_nome: str = args[0]
        self._cnpj: int = args[1]
        self._contato: int = args[2]
        self._nivel: str = args[3]
        self._nome_pai: str = args[4]
        self._pecas_vendidas: float = args[5]
        self._last_update: date = date.today()
        self._n_dist_formado: int = 0
    
    def __str__(self) -> str:

        return f'Nome: {self._dist_nome} \
        CNPJ: {self._cnpj} \
        Contato{self._contato} \
        Nível: {self._nivel} \
        Pai: {self._nome_pai} \
        Peças: {self._pecas_vendidas}\n'

    def get_dist_nome(self) -> str:
        return self._dist_nome

    def get_cnpj(self) -> int:
        return self._cnpj

    def get_contato(self) -> str:
        return self._contato

    def get_nivel(self) -> str:
        return self._nivel

    def get_nome_pai(self) -> str:
        return self._nome_pai

    def get_pecas_vendidas(self) -> float:
        return self._pecas_vendidas

    def get_n_dist_formado(self) -> int:
        return self._n_dist_formado

    def get_last_update(self) -> date:
        return self._last_update

    def set_last_update(self, last_update) -> date:
        self._last_update = last_update

    def set_nivel(self, nivel) -> str:
        self._nivel = nivel

    def get_pecas_vendidas(self, pecas_vendidas) -> float:
        self._pecas_vendidas = pecas_vendidas
