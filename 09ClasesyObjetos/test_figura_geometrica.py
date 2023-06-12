from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

cuadrado1 = Cuadrado(5, 'rojo')
print(cuadrado1)
print(cuadrado1.base)
print(cuadrado1.altura)
print(cuadrado1.color)
print(cuadrado1.calcular_area())

cuadrado1.lado = 10

print(cuadrado1.altura)
print(cuadrado1.base)
print(cuadrado1.calcular_area())

# MRO - Method Resolution Order
print(Cuadrado.mro())


rectangulo1 = Rectangulo(2,5,'verde')
print(rectangulo1)
print(rectangulo1.altura)
print(rectangulo1.base)
print(rectangulo1.color)
print(rectangulo1.calcular_area())

rectangulo1.base = 15
rectangulo1.altura = 20
rectangulo1.color = 'violeta'

print(rectangulo1)
print(rectangulo1.altura)
print(rectangulo1.base)
print(rectangulo1.color)
print(rectangulo1.calcular_area())

print(Rectangulo.mro())