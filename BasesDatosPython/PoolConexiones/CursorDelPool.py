from logger_base import root_logger
from Conexion import Conexion

class CursordelPool:

    def __init__(self) -> None:
        self._conexion: Conexion = None
        self._cursor: Conexion.cursor = None

    def __enter__(self):
        root_logger.debug('Inicio del método with __enter__')
        self._conexion: Conexion = Conexion.obtenerConexion()
        self._cursor: Conexion.cursor = self._conexion.cursor()
        return self._cursor
    
    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        root_logger.debug('Se ejecuta el método exit.')
        if valor_excepcion:
            self._conexion.rollback()
            root_logger.error(f'Ocurrió una excepcion del tipo {valor_excepcion} {tipo_excepcion} {detalle_excepcion}')
        else:
            root_logger.debug('Se hace commit de la transacción.')
            self._conexion.commit()
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)


if __name__ == '__main__':
    with CursordelPool() as cursor:
        root_logger.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM persona')
        root_logger.debug(cursor.fetchall())