import psycopg2

# Primero creamos y estableces un objeto del tipo conexión a la base de datos
conexion = psycopg2.connect(user='postgres',
                            password = 'admin',
                            host = '127.0.0.1',
                            port = '5432',
                            database = 'test_db')

# Ahora debemos de crear un objeto del tipo de cursor para ir ejecutando las demandas
cursor = conexion.cursor()

# Asiganamos la sentencia que queremos ejecutar
sentencia = 'SELECT * FROM persona'

# Ejecutamos la sentencia a través del objeto cursor
cursor.execute(sentencia)

# Creamos una variable que va a ir obteniendo todos los resultados de las acciones del cursor
registros = cursor.fetchall()

# Imprimimos los registros para visualizarlos -> Nos devuelve una lista de tuplas
print(registros)

# Cerramos el cursor y la conexión para no dejarlo abierto
cursor.close()
conexion.close()