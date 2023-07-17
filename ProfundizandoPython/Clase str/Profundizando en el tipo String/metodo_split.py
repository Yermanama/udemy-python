# Proceso inversor del método join, vamos a separar cadenas

# help(str.split)

# Retorna una lista de cadenas de la cadena que introducimos, usando el separador que le indiquemos para separarlas.
# Si no le indicamos un separador, utilizará cualquier separador en blanco que encuentre

cursos = 'Java Python Angular Spring Excel'
lista_cursos = cursos.split()

print(f'Lista de cursos -> {lista_cursos} type-> {type(lista_cursos)}')

cursos_separados_por_coma = 'Java, Python, Angular, Spring, Excel,'
lista_cursos = cursos_separados_por_coma.split()
print(f'Lista de cursos -> {lista_cursos} type-> {type(lista_cursos)}')

lista_cursos = cursos_separados_por_coma.split(',')
print(f'Lista de cursos -> {lista_cursos} type-> {type(lista_cursos)}')

# Añadimos el espacio para tener el separador correcto
lista_cursos = cursos_separados_por_coma.split(', ')
print(f'Lista de cursos -> {lista_cursos} type-> {type(lista_cursos)}')

# Vamos a indicar el parametro de max split, para determinar el número máximo de separaciones
lista_cursos = cursos_separados_por_coma.split(', ', 2)
print(f'Lista de cursos -> {lista_cursos} type-> {type(lista_cursos)}')