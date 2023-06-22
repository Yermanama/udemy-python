import psycopg2

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = (('Marcos', 'Vigo', 'mvigo@mail.com'),
                       ('Angel', 'Guevara', 'aguevara@mail.com'),
                       ('Maria', 'Gonzalez', 'mgonzalez@mail.com'))
            cursor.executemany(sentencia, valores)
            numero_registros = cursor.rowcount
            print(f'Se han añadido un total de {numero_registros} registros.')
except Exception as error:
    print(f'Ha ocurrido el error del tipo {error}')
finally:
    conexion.close()