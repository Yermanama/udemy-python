from DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):

    contador_ratones: int = 0

    @classmethod
    def asignarID(cls) -> int:
        cls.contador_ratones += 1
        return cls.contador_ratones

    def __init__(self, tipoEntrada: str, marca: str) -> None:
        super().__init__(tipoEntrada, marca)
        self._id_raton: int = self.asignarID()

    def __str__(self) -> str:
        return (f'=== Ratón ===\n'
                f'ID: {self._id_raton}\n'
                f'{super().__str__()}\n'
                f'==============')

