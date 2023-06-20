"""
Crear una función para sumar los valores recibidos de tipo numérico, 
utilizando argumentos variables *args como parámetro de la función 
y regresar como resultado la suma de todos los valores pasados como argumentos.
"""


def sumar_variables(*numeros: int) -> int :
    suma = 0
    for numero in numeros:
        suma += numero
    return suma


if __name__ == "__main__":
    print(sumar_variables(1,2,3,4,5,6,7,8,9))
