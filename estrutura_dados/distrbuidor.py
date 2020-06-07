class Distribuidor(object):
    def __init__(self, *args) -> None:
<<<<<<< HEAD
        """id , nome, cnpj, contato, nivel, nome_pai, pecas_vendidas, last_up(date)"""

        self._dist_id: int = args[0]
        self._dist_nome: str = args[1]
        self._cnpj: int = args[2]
        self._contato: int = args[3]
        self._nivel: str = args[4]
        self._nome_pai: str = args[5]
        self._pecas_vendidas: float = args[6]
        self._last_update: str
        self._n_dist_formado: int

    def get_dist_id(self) -> int:
        return self._dist_id
=======
        """ nome, cnpj, contato, nivel, nome_pai, pecas_vendidas"""

        self._dist_nome: str = args[0]
        self._cnpj: int = args[1]
        self._contato: int = args[2]
        self._nivel: str = args[3]
        self._nome_pai: str = args[4]
        self._pecas_vendidas: float = args[5]

    def __str__(self) -> str:

        return f'{self._dist_nome} \
        {self._cnpj} \
        {self._contato} \n\
        {self._nivel} \
        {self._nome_pai} \
        {self._pecas_vendidas}'
>>>>>>> 2948ea3ddca971cbdbbc8e78626f79c3198ea254

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

    def get_last_update(self) -> str:
        return self._last_update

    def set_nivel(self, nivel) -> str:
        self._nivel = nivel

    def get_pecas_vendidas(self, pecas_vendidas) -> float:
        self._pecas_vendidas = pecas_vendidas