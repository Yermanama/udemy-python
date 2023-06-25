from logger_base import root_logger as log
from psycopg2 import pool
import sys

class Conexion:

    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool == None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                    database=cls._DATABASE,
                                                    user=cls._USERNAME,
                                                    password=cls._PASSWORD,
                                                    port=cls._DB_PORT,
                                                    host=cls._HOST)
                log.debug(f'Pool de conexiones establecido correctamente. -> {cls._pool}')
                return cls._pool
            except Exception as error:
                log.error(f'Ha ocurrido un error del tipo {error}')
                sys.exit()
        else:
            return cls._pool
    

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexión establecida correctamente -> {conexion}')
        return conexion
    
    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Conexion devuelta satisfactoriamente -> {conexion}')
        
    
    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()

if __name__ == "__main__":
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    Conexion.cerrarConexiones()