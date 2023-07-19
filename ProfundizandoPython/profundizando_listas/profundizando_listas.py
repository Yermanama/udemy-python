# Profundizando en listas
# Listas son mutables

nombres1 = ['juan', 'karla', 'pedro']
nombres2 = 'laura maria gonzalo ernesto'.split()

# Sumar listas usando +
print(f'Sumar listas: {nombres1 + nombres2}')

# Extender una lista sobre otra
nombres1.extend(nombres2)  # Aquí se modifica la lista
print(f'Extendiendo la lista 1 con la lista 2', nombres1)

# lista de números
numeros = [1, 2, 3, 4, 5, 1, 4]

# Obtener el índice del primer elemento encontrado en una lista
print(f'Índice 4: {numeros.index(4)}')

# Invertir el orden de los elementos de una lista
numeros.reverse()
print(f'Lista puesta al revés: {numeros}')

# Ordenar los elementos de una lista
numeros.sort()
print(f'Lista ordenada: {numeros}')

# Ordenar los elementos de una lista de manera descendente
numeros.sort(reverse=True)
print(f'Lista ordenada de manera descendente: {numeros}')

# Obtener el valor máximo y el valor mínimo de una lista

# Valor mínimo
print(f'Valor mínimo: {min(numeros)}')

# valor máximo
print(f'Valor máximo: {max(numeros)}')

# Copiar los elementos de una lista - Con esto solo se hace una copia shallow
# Esto quiere decir que solo se copia la referencia de memoria de la lista anterior
otros_numeros = numeros.copy()

# Son objetos distintos
print(f'Misma referencia?: {numeros is otros_numeros}')

# Preguntamos si es el mismo contenido
print(f'Mismo contenido: {numeros == otros_numeros}')

# Podemos usar el contructor de la lista para crear un nuevo objeto en memoria, pero que apunta al mismo contenido
otros_numeros = list(numeros)
print(f'Misma referencia?: {numeros is otros_numeros}')
print(f'Mismo contenido?: {numeros == otros_numeros}')

# Por último podemos hacer el slicing para copiar los elementos, haciendo un nuevo objeto pero que hace referencia
# a lo mismo
otros_numeros = numeros[:]
print(f'Misma referencia?: {numeros is otros_numeros}')
print(f'Mismo contenido?: {numeros == otros_numeros}')

# Multiplicación de listas
lista_multiplicada = 5 * [[2, 5]]
print(lista_multiplicada)
print(f'Misma referencia cada uno de los objetos?: {lista_multiplicada[0] is lista_multiplicada[1]}')
print(f'Mismo contenido: {lista_multiplicada[0] == lista_multiplicada[1]}')

# Se modifican todos los elementos de la lista, porque todos apuntan a la misma referencia, por lo que se cambia todo
lista_multiplicada[2].append(10)
print(lista_multiplicada)

# Matrices en python
matriz = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
print(f'Matriz original : {matriz}')

# En este caso para recuperar cada uno de los elementos
print(f'Renglón 0, columna 0: {matriz[0][0]}')
print(f'Renglón 2, columna 3: {matriz[2][2]}')
matriz[2][0] = 'Hola'
print(matriz)

lista_listas = [[10, 14, 87, 90, 71], [4, 5, 6, 7], [9, 0, 11, 15, 45, 61, 70]]

# Vamos a ordenar por longitud de listas, es decir, primero las listas más pequeñas
lista_listas.sort(key=len)
print(f'Ordenadas por cantidad de elementos: {lista_listas}')

# Built-in sorted
nombres1 = ['Juan Carlos', 'Karla', 'Pedro', 'Esperanza']
nombres1 = sorted(nombres1)
print(f'Lista ordenada de manera ascendente: {nombres1}')
nombres1 = sorted(nombres1, reverse=True)
print(f'Lista ordenada de manera descendente: {nombres1}')

# Podemos ordenar por la cantidad de caracteres de cada nombre
nombres1 = sorted(nombres1, key=len)
print(f'Ordenada por la longitud de caracteres: {nombres1}')

# Ahora usamos built-in reversed
nombres1 = list(reversed(nombres1))
print(
    f'Antes de imprimirlo debemos de pasarlo a una lista porque reversed devuelve un objeto tipo iterable: {nombres1}')
