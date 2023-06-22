import psycopg2

conexion = psycopg2.connect(user = 'postgres', password= 'admin', host = '127.0.0.1', database = 'test_db', port = '5432')

try: 
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'select * from persona where id_persona = %s'
            id_persona = input('Proporciona el valor de id_persona: ')
            cursor.execute(sentencia, (id_persona,)) # Le pasamos un parámetro determinado para ir filtrando
            registros = cursor.fetchone() # Solo nos devuelve un registro
            print(registros)
except Exception as e:
    print(f'Error del tipo -> {e}')
finally:
    conexion.close()

