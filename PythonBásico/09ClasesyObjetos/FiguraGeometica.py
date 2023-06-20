#ABC = Abstract Base Class

from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, base, altura) -> None:
        self._base = base
        self._altura = altura

    def __str__(self) -> str:
        return f'Figura geométrica: Base -> {self._base} | Altura -> {self._altura} '
    
    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, valor):
        if valor < 0:
            raise ValueError("La base debe de ser un valor por encima de 0.")
        self._base = valor
    
    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, valor):
        if valor < 0:
            raise ValueError("La altura debe de ser mayor de 0.")
        self._altura = valor
    
    @abstractmethod
    def calcular_area(self):
        pass