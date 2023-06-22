import psycopg2

conexion = psycopg2.connect(user='postgres', password = 'admin', host = '127.0.0.1', port = '5432', database = 'test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'select * from persona where id_persona in %s'
            '''llaves_primarias = ((1,2,3),)''' # Hay que pasar el valor en tuplas de tuplas
            entrada = input('Proporciona los ids a buscar (Separado por comas)')
            llaves_primarias = (tuple(entrada.split(',')),) # Quitamos las comas, para que nos den buenos resultados debemos de hacer tupla de tuplas
            cursor.execute(sentencia, llaves_primarias)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
except Exception as e:
    print(f'Error del tipo {e}')
finally:
    conexion.close()