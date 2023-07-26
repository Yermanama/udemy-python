# es una función que define a otra y además la regresa
# la función anidada puede acceder a las variables locales definidas en la función principal o extena

# Función principal o externa

def operacion(a, b):
    # definimos la funciñon interna o anidada
    def sumar():
        return a + b
    
    # Retornamos la función 
    return sumar

mi_funcion_closure = operacion(5, 2)
print(mi_funcion_closure())

# LLama la función regresada al vuelo
print(operacion(2,3)())

# CLOSURE Y LAMBDAS 

# Podemos hacer lo anterior pero usando también las funciones lambda

def operacion(a, b):
    # definimos una funcion lambda interna y la retornamos en la misma linea de código
    return lambda: a + b

print(operacion(4,5)())