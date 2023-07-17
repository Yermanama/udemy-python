# Metodo join para los str

# help(str.join)

# Se nos idica que podemos concatenar cualquier número de strings
# El string cuyo método es llamado se inserta entre cada string pasado como parámetro

tupla_str = ('Hola', 'Mundo', 'Universidad', 'Python')

# Vamos a unirlos con un espacio entre medias

mensaje = ' '.join(tupla_str)
print(f'Mensaje -> {mensaje}')

lista_cursos = ['Python', 'java', 'angula', 'html']

# Ahora lo unimos a través de una coma 

mensaje = ', '.join(lista_cursos)
print(f'Mensaje -> {mensaje}')

cadena = 'HolaMundo'
mensaje = '.'.join(cadena)
print(f'Mensaje -> {mensaje}')

diccionario = {'nombre': 'Juan', 'apellido': 'Perez', 'edad':'18'}
llaves = '-'.join(diccionario.keys())
valores = '-'.join(diccionario.values())
print(f'Llaves -> {llaves}, type: {type(llaves)}')
print(f'Valores -> {valores}, type : {type(valores)}')