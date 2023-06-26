# bool contiene los valores de True y False

# Tipos numéricos, False para 0 y True para los demás valores

valor = 0 
print(f'El valor 0 va a dar como resultado False -> {bool(valor)}')

valor = 16
print(f'El valor 16 va a dar como resultado True -> {bool(valor)}')

valor = 0.0
print(f'En el caso de los float, el valor 0.0 va a dar como resultado False -> {bool(valor)}')

valor = 1.6
print(f'En el caso de los float, el valor 1.6 va a dar como resultado True -> {bool(valor)}')

# Tipo string, cadena vacía va a dar false, el resto true
cadena = ''
print(f'En el caso de cadena vacía el resultado es -> {bool(cadena)}')

cadena = 'hola'
print(f'En el caso de cadena llena, el resultado es -> {bool(cadena)}')


# Tipo colecciones, false para colecciones vacías, true para el resto

lista = []
print(f'Para el caso de la lista vacía, el resultado es -> {bool(lista)}')

lista = ['hola']
print(f'Para el caso de una lista llena, el resultado es {bool(lista)}')

tupla = ()
print(f'Para el caso de una tupla vacía, el resultado es {bool(tupla)}')

tupla = (1, 2)
print(f'Para el caso de una tupla llena, el resultado es -> {bool(tupla)}')

diccionario = {}
print(f'Para el caso de un diccionario vacío, el resultado es {bool(diccionario)}')

diccionario = {'hola': 1}
print(f'Para el caso de un diccionario lleno, el resultado es -> {bool(diccionario)}')
