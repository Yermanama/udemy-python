from DispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):

    contador_teclados: int = 0

    @classmethod
    def asignarID(cls):
        cls.contador_teclados += 1 
        return cls.contador_teclados
    
    def __init__(self, tipoEntrada: str, marca: str) -> None:
        super().__init__(tipoEntrada, marca)
        self._id_teclado: int = self.asignarID()

    def __str__(self) -> str:
        return (f'=== Teclado ===\n'
                f'ID: {self._id_teclado}\n'
                f'{super().__str__()}\n'
                f'==============')
