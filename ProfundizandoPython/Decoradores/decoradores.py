# Decoradores es una funcion que recibe una función y regresa otra 
# Lo usamos para extender funcionalidad

# Funcion decorador (a)
# Funcion a decorar (b)
# Funcion decorada (c)

def funcion_decorador_a(funcion_a_decorar_b):
    def funcion_decorada_c(*args, **kwargs):
        print('Hola desde la funcion decorada ')
        resultado = funcion_a_decorar_b(*args, **kwargs)
        return resultado 
    
    return funcion_decorada_c


@funcion_decorador_a
def sumar(a, b):
    return a+b

resultado = sumar(5, 6)
print(resultado)