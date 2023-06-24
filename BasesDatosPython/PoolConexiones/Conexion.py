from psycopg2 import pool
from logger_base import log
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
                                                      host = cls._HOST,
                                                      user= cls._USERNAME,
                                                      password = cls._PASSWORD,
                                                      port= cls._DB_PORT,
                                                      database = cls._DATABASE)
                log.debug(f'Gestión del pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.debug(f'Ha ocurrido un error del tipo {e}')
                sys.exit()
        else:
            return cls._pool
    

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexion obetenida del pool -> {conexion}')
        return conexion
    
    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos el objeto conexión al pool de conexiones. {conexion}')

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()


if __name__ == "__main__":
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    # conexion6 = Conexion.obtenerConexion() -> Este no funciona porque estamos por encima del número maximo que de conexiones que se pueden hacer del pool
    