import psycopg2 as bd

conexion = bd.connect(user='postgres', password = 'admin', host= '127.0.0.1', port = '5432', database = 'test_db')

try:
    conexion.autocommit = False
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    valores = ('Maria', 'Esperanza', 'mesperanza@mail.com')
    cursor.execute(sentencia, valores)

    sentecia_upsert = '''
    INSERT INTO persona(id_persona, nombre, apellido, email) 
    VALUES(%s, %s, %s, %s)
    ON CONFLICT (id_persona)
    DO UPDATE SET nombre = EXCLUDED.nombre, apellido=EXCLUDED.apellido, email=EXCLUDED.email
    '''
    valores_upsert = (1, 'Juan Carlos', 'Juarez', 'jcjuarez@mail.com')
    cursor.execute(sentecia_upsert, valores_upsert)

    conexion.commit()
    print('Transaccion terminada')

except Exception as e:
    conexion.rollback()
    print(f'''Ha habido un error del tipo {e}
        Se hace un rollback para no afectar a la base de datos.''')
    
finally:
    conexion.close()
