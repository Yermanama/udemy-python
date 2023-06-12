from FiguraGeometica import FiguraGeometrica
from Color import Color

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, base, altura, color) -> None:
        FiguraGeometrica.__init__(self, base=base, altura = altura)
        Color.__init__(self, color=color)

    def __str__(self) -> str:
        return FiguraGeometrica.__str__(self) + Color.__str__(self) + f' Tipo Rectángulo'
    
    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, valor):
        if valor < 0:
            raise ValueError("El valor debe de ser mayor que 0.")
        self._base = valor

    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, valor):
        if valor < 0:
            raise ValueError("El valor debe de ser mayor de 0.")
        self._altura = valor

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, valor):
        self._color = valor

    def calcular_area(self):
        return self._altura * self._base