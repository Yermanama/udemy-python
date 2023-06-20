from Monitor import Monitor
from Teclado import Teclado
from Raton import Raton


class Computadora():

    contador_computadoras: int = 0

    @classmethod
    def asignarID(cls) -> int:
        cls.contador_computadoras += 1
        return cls.contador_computadoras
    
    def __init__(self, nombre: str, monitor: Monitor, teclado: Teclado, raton: Raton) -> None:
        self._id_computadora = self.asignarID()
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton


    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_valor):
        self._nombre = nuevo_valor

    @property
    def monitor(self):
        return self._monitor
    
    @monitor.setter
    def monitor(self, nuevo_monitor: Monitor):
        self._monitor = nuevo_monitor

    @property
    def teclado(self):
        return self._teclado
    
    @teclado.setter
    def teclado(self, nuevo_teclado: Teclado):
        self._teclado = nuevo_teclado

    @property
    def raton(self):
        return self._raton
    
    @raton.setter
    def raton(self, nuevo_raton: Raton):
        self._raton = nuevo_raton

    def __str__(self) -> str:
        return (f'=== Computadora ===\n'
                f'ID: {self._id_computadora}\n'
                f'Nombre: {self._nombre}\n'
                f'Monitor: \n{self._monitor}\n'
                f'Teclado: \n{self._teclado}\n'
                f'Ratón: \n{self._raton}\n'
                f'==================')
