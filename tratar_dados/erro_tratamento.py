import logging


class ErroTratamento(Exception):
    def __init__(self, msg) -> None:
        self._msg = msg
        logging.error('ERRO: ' + msg)

    def get_msg(self) -> str:
        return self._msg
