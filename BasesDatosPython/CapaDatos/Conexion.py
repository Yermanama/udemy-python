from logger_base import log 
import psycopg2 as bd
import sys

class Conexion:

    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion == None:
            try:
                cls._conexion = bd.connect(database= cls._DATABASE, user=cls._USERNAME, password=cls._PASSWORD, port=cls._DB_PORT, host=cls._HOST)
                log.debug(f'Conexión exitosa -> {cls._conexion}')
                return cls._conexion
            except Exception as e:
                print(f'Ha ocurrido un error del tipo {e}')
                sys.exit()
        else:
            return cls._conexion
        
    @classmethod
    def obtenerCursor(cls):
        if cls._cursor == None:
            try:
                cls._cursor = cls._conexion.cursor()
                print(f'Cursor establecido correctamente -> {cls._cursor}')
                return cls._cursor
            except Exception as e:
                print(f'Ha ocurrido un error del tipo {e}')
                sys.exit()
        else: 
            return cls._cursor
        
if __name__ == "__main__":
    Conexion.obtenerConexion()
    Conexion.obtenerCursor()
                      

