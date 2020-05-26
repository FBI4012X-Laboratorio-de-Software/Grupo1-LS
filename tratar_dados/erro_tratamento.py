class ErroTratamento(Exception):
    def __init__(self, msg) -> None:
        self._msg = msg

    def get_msg(self) -> str:
        return self._msg
