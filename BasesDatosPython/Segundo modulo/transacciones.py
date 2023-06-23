import psycopg2 as bd

conexion = bd.connect(user= 'postgres', password= 'admin', host = '127.0.0.1', port='5432', database= 'test_db')

try:
    # Debemos de saber que si usamos WITH todas las transacciones se hacen de manera automática
    # Se hacen commits si todo está bien, o se hace un rollback si alguno de los query están mal
    # Indicammos que no queremos que se hagan las cosas de manera automática
    conexion.autocommit = False
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    valores = ('Maria', 'Esparza', 'mesparza@mail.com')
    cursor.execute(sentencia, valores)
    # Ahora añadimos esta sentencia para realizar el commit
    conexion.commit()
    print('Termina la transaccion')

except Exception as e:
    conexion.rollback()
    print(f'Ha ocurrido un error del tipo -> {e}')
    print('Se ha hecho un rollback para que no haya ningún problema')
finally:
    conexion.close()