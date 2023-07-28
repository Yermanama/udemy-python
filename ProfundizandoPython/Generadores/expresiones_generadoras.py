# Expresión generadora - Es un generador anónimo

multiplicacion = (valor*valor for valor in range(4))

print(multiplicacion) # Podemos ver que es un objeto de tipo generador
print(type(multiplicacion))

print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))

# También se puede pasar una expresión generador a una función (sin paréntesis)

import math
suma = sum(valor*valor for valor in range(4))
print(suma)
print(type(suma))

print(f'Resultado suma {suma}')