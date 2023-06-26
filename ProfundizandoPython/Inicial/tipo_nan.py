import math
from decimal import Decimal

# manejo de valores tipo nan -> Significa not a number
# Es un tipo de dato numérico para representar un dato numérico indefinido

a = float('nan')
print(f'Generación de un NaN a través de float -> {a}')
print(f'Comprobación a través del módulo math, ¿es un Nan? -> {math.isnan(a)}')

a = float(3.14)
print(f'Generación de un número para comprobar si es Nan -> {a}')
print(f'Comprobación a través del módulo math, ¿es un Nan? -> {math.isnan(a)}')

a = Decimal('NaN')
print(f'Generación de un valor Nan a través del objeto Decimal del módulo decimal -> {a}')
print(f'Comprobación a través del módulo math, ¿es un Nan? -> {math.isnan(a)}')
