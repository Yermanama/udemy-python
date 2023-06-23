import psycopg2

conexion = psycopg2.connect(user= 'postgres', password= 'admin', host= '127.0.0.1', port = '5432', database= 'test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
            entrada = input('Introduce los valores de los id de las personas que quieres eliminar, seperados por coma: ')
            valores = (tuple(entrada.split(',')),)
            cursor.execute(sentencia, valores)
            print(f'Se han eliminado {valores} valores.')
except Exception as error:
    print(f'Se ha cometido un error del tipo {error}')
finally: 
    conexion.close()