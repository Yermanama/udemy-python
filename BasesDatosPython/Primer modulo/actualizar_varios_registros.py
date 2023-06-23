import psycopg2

conexion = psycopg2.connect(user='postgres', password='admin', port='5432', host='127.0.0.1', database= 'test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = (
                ('Juan', 'Pérez', 'jperez@mail.com', 1),
                ('Ivonne', 'Gutierrez', 'igutierrez@mail.com', 2))
            cursor.executemany(sentencia, valores)
            print(f'Numero de registros actualizados -> {cursor.rowcount}')
except Exception as error:
    print(f'No se ha podido realizar la actualización por un error del tipo -> {error}')
finally:
    conexion.close()

