# Lista de listas

lista_listas = [[1,2,3], [4,5,6], [7,8,9]]

# Convertimos la lista de listas en una lista simple
lista_simple = [sublista for sublista in lista_listas ]
print(f'Primer paso de conversión sería este: {lista_simple}')

# Ahora vamos a hacerlo completo
lista_listas = [[1,2,3], [4,5,6], [7,8,9]]
lista_simple = [valor for sublista in lista_listas for valor in sublista]
print(lista_simple)

# Ahora vamos a crear una nueva lista de numeros pares a partir de la lista de listas
# Sin list comprehensions, ciclos for anidados
lista_pares = []
for sublista in lista_listas:
    for valor in sublista:
        if valor %2 == 0:
            lista_pares.append(valor)

print(lista_pares)

# Con list comprehensions
lista_pares = [valor*valor for sublista in lista_listas for valor in sublista if valor%2 == 0]
print(lista_pares)