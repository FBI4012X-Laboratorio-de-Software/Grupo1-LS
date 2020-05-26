class Distribuidor(object):
    def __init__(self, *args) -> None:
        """id , nome, cnpj, contato, nivel, nome_pai, pecas_vendidas"""

        self._dist_id: int = args[0]
        self._dist_nome: str = args[1]
        self._cnpj: int = args[2]
        self._contato: int = args[3]
        self._nivel: str = args[4]
        self._nome_pai: str = args[5]
        self._pecas_vendidas: float = args[6]

    def get_dist_id(self) -> int:
        return self._dist_id

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
