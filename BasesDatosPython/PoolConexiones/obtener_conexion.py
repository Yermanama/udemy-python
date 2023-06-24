from psycopg2 import pool
from logger_base import root_logger
import sys

class Conexion:

    _DATABASE = 'test_db'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _MIN = 1
    _MAX = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool == None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN, cls._MAX,
                                                      database = cls._DATABASE,
                                                      port= cls._DB_PORT,
                                                      user= cls._USERNAME,
                                                      host= cls._HOST,
                                                      password= cls._PASSWORD)
                root_logger.debug(f'Pool obtenido satisfactoriamente. -> {cls._pool}')
                return cls._pool
            except Exception as e:
                root_logger.debug(f'Ha habido un error del tipo -> {e}')
                sys.exit()
        else:
            return cls._pool
    
    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        root_logger.debug(f'Se ha obtenido una conexión exitosa -> {conexion}')
        return conexion
    
    @classmethod
    def liberarConexion(cls, conexion):
        Conexion.obtenerPool().putconn(conexion)
        root_logger.debug(f'Hemos liberado la conexion -> {conexion}')


    @classmethod
    def cerrarConexiones(cls):
        Conexion.obtenerPool().closeall()
        root_logger.debug('Se han cerrado todas las conexiones del pool.')


if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion=conexion1)
    Conexion.cerrarConexiones()

    