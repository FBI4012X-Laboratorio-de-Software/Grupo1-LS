from datetime import datetime


class Vendas(object):
    def __init__(self, *args) -> None:
        """data, valor venda, id distribuidor"""
        self._data: datetime = args[0]
        self._valor_venda: float = args[1]
        self._id_distribuidor: int = args[2]

    def __str__(self) -> str:

        return f'{self._data} \
            {self._valor_venda} \
            {self._id_distribuidor}'

    def get_data(self) -> datetime:
        return self._data

    def get_valor_venda(self) -> float:
        return self._valor_venda

    def get_id_distribuidor(self) -> int:
        return self._id_distribuidor
