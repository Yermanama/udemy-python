# No se pueden modificar las cadenas

# help(str.capitalize)

mensaje1 = 'hola mundo'
mensaje2 = mensaje1.capitalize()

print(f'Imprimimos la variable mensaje1 -> {mensaje1} -> id: {id(mensaje1)}')
print(f'Imprimimos la variable mensaje2 -> {mensaje2} -> id: {id(mensaje2)}')

mensaje1 += 'adios'
print(f'Mensaje 1 -> {mensaje1} -> id {id(mensaje1)} -> Ha cambiado la dirección de memoria, por lo que es un objeto nuevo')