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