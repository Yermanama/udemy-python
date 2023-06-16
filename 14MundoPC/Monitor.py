class Monitor:

    contador_monitores: int = 0

    @classmethod
    def asignarID(cls) -> int :
        cls.contador_monitores += 1
        return cls.contador_monitores
    
    def __init__(self, marca: str, tamano: str) -> None:
        self._id_monitor: int = self.asignarID()
        self._marca: str = marca
        self._tamano: str = tamano  


    @property
    def marca(self):
        return self._marca
    

    @marca.setter
    def marca(self, nuevo_valor: str):
        self._marca = nuevo_valor
    

    @property
    def tamano(self):
        return self._tamano
    

    
    @tamano.setter
    def tamano(self, nuevo_valor: str):
        self._tamano = nuevo_valor

    
    def __str__(self) -> str:
        return (f'=== Monitor ===\n'
                f'ID: {self._id_monitor}\n'
                f'Marca: {self._marca}\n'
                f'Tamaño: {self._tamano}\n'
                f'==============')
