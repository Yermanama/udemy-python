from pprint import pprint as pp

# Los diccionarios guardan un orden (a diferencia de un set)

diccionario = {"Nombre": "Juan", "Apellido": "Perez", "Edad": 28}
print(diccionario)

# Los diccionarios son mutables pero sus llaves no pueden serlo
# diccionario = {[1,2]: 'Valor 1'} -> Esto da error puesto una lista es mutable y no puede usarse como llave

# Lo que si se podría hacer es pasarlo a ser, que no es mutable
diccionario = {(1,2): 'Valor 1'}
print(diccionario)

# En el caso de que pongamos una llave que no esté en el diccionario, lo añade automáticamente
diccionario['Departamento'] = 'Sistemas'
print(diccionario)

# Los diccionarios no tienen valores duplicados en las llaves de un diccionario, si ya existe, se reemplaza
diccionario["Departamento"] = 'Programación'
print(diccionario)

diccionario['Departamentos'] = 'De control'
print(diccionario)


# Recuperar un valor indicando el valor de la llave
print(diccionario['Departamento'])

# De la manera anterior si no encuentra la llave lanza una excepción
# print(diccionario['Pepito'])

# Ahora usando el método get, recupera el valor, y si no existe la llave, no salta excepción y además podemos hacer que devuelva un valor por default
print(diccionario.get('Nombre', 'No se ha encontrado la llave'))
print(diccionario.get('Departamento', 'No se ha encontrado la llave'))

# Metodo setdefault si modifica el diccionario en el caso de que no se encuentre la llave, y se puede agregar un valor por default
nombre = diccionario.setdefault('Nombres', 'No se encontró el valor')
print(nombre)
print(diccionario)

# manera simple de imprimir un diccionnario, función pprint
# sort dicts nos permite ordenar el diccionario
pp(diccionario)
pp(diccionario, sort_dicts=False)

