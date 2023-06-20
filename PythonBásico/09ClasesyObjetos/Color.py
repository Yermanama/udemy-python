class Color:
    def __init__(self, color: str) -> None:
        self._color: str = color

    def __str__(self) -> str:
        return f'Color -> {self._color}'

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, valor: str):
        self.color = valor