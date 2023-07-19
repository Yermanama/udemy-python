# El asterisco * nos sirve para desempaquetar (unpacking)
numeros = [1, 2, 3]
print(numeros)

# Con unpacking podemos imprimir cada uno de los elementos de la lista
print(*numeros)
print(*numeros, sep='-')


# Esto lo podemos aplicar a cualquier iterable, en el caso del diccionario, debemos de usar doble asterisco


def sumar(a, b, c):
    print(f'Resultado de la suma: {a + b + c}')


# Podemos pasar la lista con unpacking de manera que se pase cada uno de los objetos de la lista
sumar(*numeros)

# Extraer algunos elementos de una lista
mi_lista = [1, 2, 3, 4, 5, 6]
a, *b, c, d = mi_lista
print(a, b, c, d)

# Unir listas con unpacking
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

lista3 = [lista1, lista2]  # Esto es una lista de listas, pero no queremos eso ahora
print(lista3)

lista3 = [*lista1, *lista2]  # Se desempaquetan y se añaden a la lista3
print(lista3)

# Unir diccionarios con unpacking
dic1 = {'a': 1, 'b': 2, 'c': 3}
dic2 = {'d': 4, 'e': 5}
dic3 = {**dic1, **dic2}
print(dic3)

# Construir una lista a partir de un string
lista = [*'Hola mundo']
print(lista)
print(*lista)
