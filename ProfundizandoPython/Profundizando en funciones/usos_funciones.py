# Las funciones en python son ciudadanas de primera clase
# First class citizens
# Son como objetos, por lo que podemos hacer los usos que vamos a tener de los objetos

# Definimos la función

def sumar(a, b):
    return a + b

# Podemos asignar la función a una variable, que lo debemos de hacer sin paréntesis, porque queremos aisgnar y no ejecutar

mi_funcion = sumar
print(mi_funcion(2, 2))


# Función como argumento

def operacion(a, b, sumar):
    print(f'Resultado sumar: {sumar(a, b)}')

operacion(2, 3, sumar)

# Podemos retornar una función

def retornar_funcion():
    # retornamos una función
    return sumar


mi_funcion_retornada = retornar_funcion()

print(f'REsultado de la función retornada : {mi_funcion_retornada(1, 2)}')