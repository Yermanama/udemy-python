class Cubo():
    def __init__(self) -> None:
        self.ancho = int(input("Proporciona el ancho por favor: "))
        self.alto = int(input("Proporciona el alto por favor: "))
        self.profundidad = int(input("Proporciona la profundidad: "))
    
    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundidad
    
cubo1 = Cubo()
print(f"El volumen del cubo es de: {cubo1.calcular_volumen()}")