import psycopg2

conexion = psycopg2.connect(user='postgres', password = 'admin', port = '5432', host = '127.0.0.1', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona = %s'
            valores = input('Proporciona el número del id de la persona que quieres eliminar')
            cursor.execute(sentencia, valores)
            print(f'Se han eliminado {cursor.rowcount} valores.')
except Exception as error:
    print(f'Se ha cometido un error del tipo -> {error}')
finally:
    conexion.close()