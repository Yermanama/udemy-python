# Mas de funciones anidadas y alcance de variables

def funcion_externa():
    variable_local_externa = 'Variablel local externa'


    def funcion_anidada():
        # SI queremos trabajar con una variable que no es local, pero que fue definida en bloque de código no global, debemos de usar nonlocal
        nonlocal variable_local_externa
        # Porque si no se crearía una nueva variable
        variable_local_anidada = 'Variable local anidada'
        variable_local_externa = 'Nuevo valor de la variable local externa'

    funcion_anidada()

    print(f'Valor variabel local externa {variable_local_externa}')


funcion_externa()