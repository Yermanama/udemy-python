# Profundizando en tuplas
# Es inmutable

# Declarar variables
a, b = 'Hola', 'Adios'  # Esto es una tupla, y lo que estamos haciendo es unpacking
print(a, b)

# swap (intercambio) -> Cambiamos el valor de cada una de las variables
a, b = b, a
print(a, b)


# Regresar múltiples valores en una función
def minmax(elementos):
    return min(elementos), max(elementos)


minimo, maximo = minmax([1, 2, 3, 4, 5])
print(f'El valor mínimo es {minimo}, y el valor máximo es: {maximo}')

# Regresa la suma de una tupla
resultado = sum((1, 2, 3, 4, 5))
print(f'Resultado: {resultado}')


def sumar(*args):
    return sum(args)


resultado = sumar(1, 2, 3, 4, 5)
print(f'Resultado sumar: {resultado}')