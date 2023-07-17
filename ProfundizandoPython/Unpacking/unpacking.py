# Desempaquetar en python

# Aquí vemos que se crea una tuple de valores
valores = 1, 2, 3
print(valores)
print(type(valores))

# Vamos a desempaquetar
valor1, valor2, valor3 = 1, 2, 3
print(valor1)
print(valor2)
print(valor3)

# Si no quiero asignar pongo un guión
valor1, _, valor3 = 4, 5, 6
print(valor1)
print(_)  # Lo que pasa es que no lo vamos a usar a lo largo del programa
print(valor3)


# Si lo que quiero es que solo se desempaqueten los primeros valores y el resto en uno debo de hacer lo siguiente
valor1, valor2, *valor3 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(valor1)
print(valor2)
print(valor3)

# Podemos también seleccionar los últimos valores
valor1, valor2, *valor3, valor4, valor5 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(valor1, valor2, valor3, valor4, valor5)

# También podemos desempaquetar asignando los valores a una lista
valor1, valor2, *valor3, valor4, valor5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(valor1, valor2, valor3, valor4, valor5)


def regresa_varios_datos():
    return 1, 2, 3


valor1, valor2, valor3 = regresa_varios_datos()
print(valor1, valor2, valor3)

valor1, *_ = regresa_varios_datos()
print(valor1)
print(_)

variable = '17:20'.partition(':')
print(variable)
hora, _, minutos = variable
print(hora)
print(minutos)
