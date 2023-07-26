# Funciones anonimas, y son pequeñas, con una sola línea de código


# NO es posible asignar una función a una variable de esta manera 
def sumar(a ,b):
    return a + b

# Pero de esta manera si que se puede, pero no es lo mejor
funcion = sumar

# Con una función lambda (anónima, sin nombre, y en una sola línea)
# No se necesita agregar paréntesis para los parámetros
# NO se nevesita usar la palabra return, pero sé debe regresar una expresión

mi_funcion_lambda = lambda a, b: a + b

resultado = mi_funcion_lambda(2, 3)
print(resultado)

# Función lambda que no recibe argumentos pero si que recibe una expresión
mi_funcion_lambda = lambda: 'función sin argumentos'
print(mi_funcion_lambda())

# Parametros por default

mi_funcion_lambda = lambda a=3, b=2 : a +b
print(mi_funcion_lambda())
print(mi_funcion_lambda(5,5))

# con argumentos variabes, args kwargs
mi_funcion_lambda = lambda *args, **kwargs: len(args) + len(kwargs)

print(mi_funcion_lambda(1, 2, 3, a=5, b=5))

# combinando todo
mi_funcion_lambda = lambda a, b, c=3, *args, **kwargs: a +b+c + len(args) + len(kwargs)
print(mi_funcion_lambda(1, 2, 4, 5, 6, 7, e=5, f=7))
