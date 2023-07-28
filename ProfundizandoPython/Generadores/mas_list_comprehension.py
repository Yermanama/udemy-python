# Ejemplo con dos condiciones (sabiendo que son opcionales)
# Solo se agrega el valor a la lista cuando el valor cumple ambas condiciones
# En este caso, debe de ser divisible entre dos y divisible entre 6

pares = [numero for numero in range(50) if numero%2 == 0 and numero%6 == 0]
print(pares)

# Ahrora vamos a usar if else
lista_pares = []
lista_impares = []

for numero in range(10):
    if numero %2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

print(f'Lista pares: {lista_pares}')
print(f'Lista impares: {lista_impares}')

# Ahora vamos a hacer el mismo ejercicio pero usando list comprehension
lista_pares = []
lista_impares = []

[lista_pares.append(numero) if numero%2 == 0 else lista_impares.append(numero) for numero in range(10)]

print(f'Lista pares con comprehension: {lista_pares}')
print(f'Lista impares con comprehension: {lista_impares}')