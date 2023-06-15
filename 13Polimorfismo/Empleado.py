class Empleado:
    def __init__(self, nombre, sueldo) -> None:
        self._nombre: str = nombre
        self._sueldo: int = sueldo

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_valor):
        self._nombre = nuevo_valor
    
    @property
    def sueldo(self):
        return self._sueldo
    
    @sueldo.setter
    def sueldo(self, nuevo_valor):
        self._sueldo = nuevo_valor

    def __str__(self) -> str:
        return f'Empleado: [Nombre: {self._nombre} | Sueldo: {self._sueldo}]'