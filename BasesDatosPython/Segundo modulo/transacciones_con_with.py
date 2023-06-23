import psycopg2 as bd

conexion = bd.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia_upsert = '''
            INSERT INTO persona(id_persona, nombre, apellido, email)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (id_persona)
            DO UPDATE SET nombre=EXCLUDED.nombre, apellido=EXCLUDED.apellido, email =EXCLUDED.email
            '''
            valores = (2, 'German', 'Martinez', 'gmartinez@mail.com')
            cursor.execute(sentencia_upsert, valores)
            print('Se ha realizado la transacción')
except Exception as e:
    print(f'Ha habido un erro del tipo {e}')
    print('Se va a hacer rollback')
finally:
    conexion.close()