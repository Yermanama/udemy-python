# List comprehension 

numeros = range(10)
lista_pares = []

# Creamos una nueva lista con los valores pares multiplicados por si mismos
for numero in numeros:
    # Revisamos si es un número par
    if numero%2 == 0:
        lista_pares.append(numero*numero)
    
print(f'Lista pares multiplicados por si mismos: {lista_pares}')

# Ahora vamos a hacer el mismo ejercicio pero realizando list comprehensions
# La sintaxis es la sisguiente :
# [expresion for var in colección if condición]
# La condición es opcional

lista_pares = [numero*numero for numero in range(10) if numero%2 == 0]
print(lista_pares)