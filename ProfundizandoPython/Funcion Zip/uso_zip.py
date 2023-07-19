# Uso de la función zip

numeros = [1, 2, 3, 4]
letras = ['a', 'b', 'c']
mezcla = zip(numeros, letras)
print(mezcla)  # Esto nos da un objeto tipo zip
# Para poder iterar sobre él, debemos de pasarlo a un objeto iterable, como puede ser una tupla o una lista
print(tuple(mezcla))
mezcla = zip(numeros, letras)
print(list(mezcla))

# Se van a tomar solo los primeros valores debido a que se cogen solo la cantidad del conjunto más pequeño
identificadores = 321, 322, 323, 324, 325
mezcla = zip(numeros, letras, identificadores)
print(tuple(mezcla))

# Debemos de saber si lo hacemos con un set, no vamos a poder tomar los primeros elementos, ya que no están ordenadas
conjunto = {1, 2, 3, 4, 5, 6}
print(list(zip(numeros, letras, identificadores, conjunto)))

# Iterar en paralelo
for numero, letra, identificador, aleatorio in zip(numeros, letras, identificadores, conjunto):
    print(f'Numero: {numero}, letra: {letra}, id: {identificador}, aleatorio: {aleatorio}')

nueva_lista = []
for numero, letra, identificador, aleatorio in zip(numeros, letras, identificadores, conjunto):
    nueva_lista.append(f'{identificador}-{numero}-{letra}-{aleatorio}')

print(nueva_lista)

# Proceso unzip (Podemos usar unpacking más zip para hacerlo)
mezcla = [(1, 'a'), (2, 'b'), (3, 'c')]
numeros, letras = zip(*mezcla)
# Lo que se hace aquí es que se separan y se cogen por separado los valores, y se juntan en dos listas distintas
print(numeros)
print(letras)


# Ordenando usando zip
letras = ['c', 'd', 'a', 'e', 'b']
numeros = [3, 4, 1, 2, 0]
mezcla = zip(letras, numeros)
# Sin orden
print(tuple(mezcla))

# Ordenar por letra - DEBEMOS DE SABER QUE SE ORDENAN SEGÚN EL PRIMER ITERADOR QUE LE PASEMOS
print(sorted(zip(letras, numeros)))

# Ordenar por numero
print(sorted(zip(numeros, letras)))


# Crear un diccionario a partir de dos iterables y la función zip
llaves = ['Nombre', 'Apellido', 'Edad']
valores = ['Juan', 'Perez', 18]
diccionario = dict(zip(llaves, valores))
print(diccionario)

# Actualizar un elemento de un diccionario
llave = ['Edad']  # Debemos de usar un elemento iterable, aunque sea solo una lista con un solo valor
nueva_edad = [28]
diccionario.update(zip(llave, nueva_edad))
print(diccionario)