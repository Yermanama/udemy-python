import psycopg2

conexion = psycopg2.connect(user='postgres', password='admin', host= '127.0.0.1', port = '5432', database='test_db')

try: 
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido= %s, email=%s WHERE id_persona=%s'
            valores= ('Juan Carlos', 'Jiménez', 'jcjimenez@mail.com', 1)
            cursor.execute(sentencia, valores)
            print(f'Numero de registros actualizados {cursor.rowcount}')
except Exception as error:
    print(f'Tenemos un error del tipo -> {error}')
finally:
    conexion.close()

