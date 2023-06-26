import math
from decimal import Decimal

# Manejor de valores infinitos

infinito_positivo = float('inf')

print(f'Infinito positivo a través de float: {infinito_positivo}')
print(f'¿Es este valor infinito? -> {math.isinf(infinito_positivo)}')

string_infinito = 'inf'
# print(f'¿Es este valor infinito? -> {math.isinf(string_infinito)}')
# Da error porque necesitamos un valor numérico

numero_float = 12.12
print(f'¿Es este valor infinito? -> {math.isinf(infinito_positivo)}')

infinito_negativo = float('-inf')
print(f'Valor infinito negativo a través de float -inf -> {infinito_negativo}')
print(f'¿Es este valor infinito? -> {math.isinf(infinito_negativo)}')

# A través del módulo de math podemos crear también las representaciones de números infinitos
infinito_positivo = math.inf
print(f'Infinito positivo a través de módulo math: {infinito_positivo}')
print(f'¿Es este valor infinito? -> {math.isinf(infinito_positivo)}')

infinito_negativo = -math.inf
print(f'Valor infinito negativo a través de módulo math, -math.inf -> {infinito_negativo}')
print(f'¿Es este valor infinito? -> {math.isinf(infinito_negativo)}')

# También podemos generar una representación del infinito a través del módulo decimal
infinito_positivo = Decimal('Infinity')
print(f'Infinito positivo a través de módulo decimal con Infinity: {infinito_positivo}')
print(f'¿Es este valor infinito? -> {math.isinf(infinito_positivo)}')

infinito_negativo = Decimal('-Infinity')
print(f'Valor infinito negativo a través de módulo math, Decimal(-Infinity) -> {infinito_negativo}')
print(f'¿Es este valor infinito? -> {math.isinf(infinito_negativo)}')