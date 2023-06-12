from FiguraGeometica import FiguraGeometrica
from Color import Color


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color) -> None:
        FiguraGeometrica.__init__(self, base=lado, altura=lado)
        Color.__init__(self,color)


    def __str__(self) -> str:
        return FiguraGeometrica.__str__(self) + Color.__str__(self) + f' Tipo Cuadrado'

    @property
    def lado(self):
        return self._base
    
    @lado.setter
    def lado(self, valor):
        if valor < 0:
            raise ValueError("El valor del lado del cuadrado debe de ser mayor de 0.")
        self._base = valor
        self.altura = valor

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, valor: str):
        self._color = valor

    def calcular_area(self):
        return self._altura * self._base
    
    