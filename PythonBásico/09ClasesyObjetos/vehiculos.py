"""
Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Coche y Bicicleta,
las cuales heredan de la clase Padre Vehiculo.
La clase padre debe tener los siguientes atributos y métodos

Vehiculo (Clase Padre):
-Atributos (color, ruedas)
-Métodos ( __init__() y __str__ )

Coche  (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo):
-Atributos ( velocidad (km/hr) )
-Métodos ( __init__() y __str__() )

Bicicleta  (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo):
-Atributos ( tipo (urbana/montaña/etc )
-Métodos ( __init__() y __str__() )
"""

class Vehiculo:
    def __init__(self, color: str, ruedas: int) -> None:
        self.color: str = color
        self.ruedas: int = ruedas
    
    def __str__(self) -> str:
        return f'Vehiculo[Color -> {self.color} | Ruedas -> {self.ruedas}]'


class Coche(Vehiculo):
    def __init__(self, color: str, ruedas: int, velocidad: int) -> None:
        super().__init__(color, ruedas)
        self.velocidad: int = velocidad
    
    def __str__(self) -> str:
        return super().__str__() + f' Coche[Velocidad -> {self.velocidad}km/h]'


class Bicicleta(Vehiculo):
    def __init__(self, color: str, ruedas: int, tipo: str) -> None:
        super().__init__(color, ruedas)
        self.tipo: str = tipo

    def __str__(self) -> str:
        return super().__str__() + f' Bicicleta[Tipo -> {self.tipo}]'
    

vehiculo_prueba = Vehiculo(color='Rojo', ruedas='3')
print(vehiculo_prueba)

coche_rapido = Coche(color='Blanco', ruedas=3, velocidad= 150)
print(coche_rapido)

bicicleta_carretera = Bicicleta(color='Verde', ruedas = 2, tipo= 'Carretera')
print(bicicleta_carretera)