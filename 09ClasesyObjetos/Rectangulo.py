class Rectangulo():
    def __init__(self) -> None:
        self.base = int(input("Proporciona la base del rectángulo: "))
        self.altura = int(input("Proporciona la altura del rectángulo: "))
    
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimtero(self):
        return (self.base * 2) + (self.altura * 2)
    

rectangulo1 = Rectangulo()
print(f"Area: {rectangulo1.calcular_area()}")
print(f"Perímetro: {rectangulo1.calcular_perimtero()}")

rectangulo2 = Rectangulo()
print(f"Area: {rectangulo2.calcular_area()}")
print(f"Perímetro: {rectangulo2.calcular_perimtero()}")
