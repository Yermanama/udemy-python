class DispositivoEntrada:
    def __init__(self, tipoEntrada: str, marca: str) -> None:
        self._tipo_entrada: str = tipoEntrada
        self._marca: str = marca
        
    @property
    def tipo_entrada(self):
        return self._tipo_entrada
    
    @tipo_entrada.setter
    def tipo_entrada(self, nuevo_valor: str):
        self._tipo_entrada = nuevo_valor

    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, nuevo_valor: str):
        self._marca = nuevo_valor

    def __str__(self) -> str:
        return (f'=== Dispositivo de Entrada ===\n'
                f'Tipo de entrada: {self._tipo_entrada}\n'
                f'Marca: {self._marca}\n'
                f'==============================')
