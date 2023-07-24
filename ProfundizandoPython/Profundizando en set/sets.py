# Profundizar en sets
# Un set es una coleccion de elementos únicos y además es mutable (NO REPETIDOS)
# Los elementos de un set deben de ser inmutables (NO VAN A PODER ALMACENAR LISTAS, PUESTO SON MUTABLES)

conjunto = {'Juan', True, 18, 18.0}
print(conjunto)

# Set vacío
conjunto = {}
print(type(conjunto))  # Esto no crea un set, crea un dict

# La manera correcta es la siguiente
conjunto = set()
print(type(conjunto))


# Para añadir elementos a un conjunto -> add
conjunto.add('Juan')
print(conjunto)
conjunto.add('Juan')  # No admite duplicados
print(conjunto)


conjunto = set([4, 5, 6, 7, 8, 4]) # Se eliminará los valores duplicados
print(conjunto)

# Podemos agregar más elementos, e incluso otro set al set definido
conjunto2 = {100, 200, 300, 100}
conjunto.update(conjunto2)
print(conjunto)

# Copiar un set (copo poco profunda, solo copia las referencias)
copia = conjunto.copy()
print(copia)
print(f'Es igual en contenido?: {conjunto == copia}')
print(f'Es el mismo objeto/referencia?: {conjunto is copia}')


pelo_negro = {'Juan', 'Karla', 'Pedro', 'Maria'}
pelo_rubio = {'Lorenzo', 'Laura', 'Marco'}
ojos_cafe = {'Karla', 'Laura'}
menores_30 = {'Juan', 'Karla', 'Maria'}

# Operaciones algebraicas con los sets

# Union
print(ojos_cafe.union(pelo_rubio))  # Se puede invertir el orden que el resultado va a ser el mismo

# Intersection
print(ojos_cafe.intersection(pelo_rubio))  # También es una operación conmutativa

# Difference
print(pelo_negro.difference(ojos_cafe))  # Esta no es conmutativa

# Symmetric Difference OR
print(pelo_negro.symmetric_difference(ojos_cafe))  # Esta es conmutativa


# Preguntas con set

# Subset (Si el conjunto está dentro de otro)
# Revisamos son los elementos de un conjunto está dentro del otro set
print(menores_30.issubset(pelo_negro))

# Superset (Si un conjunto puede tener al otro dentro)
print(menores_30.issuperset(pelo_negro))
print(pelo_negro.issuperset(menores_30))

# Si no coinciden los dos conjuntos en nada
print(pelo_negro.isdisjoint(pelo_rubio))
