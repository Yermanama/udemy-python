from logger_base import root_logger as log
from Conexion import Conexion
import sys

class CursorDelPool:

    def __init__(self) -> None:
        self._conn = None
        self._cursor = None

    def __enter__(self):
        log.debug('Dentro del bloque ENTER')
        self._conn = Conexion.obtenerConexion()
        self._cursor = self._conn.cursor()
        return self._cursor
    
    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        log.debug('Dentro del bloque EXIT')
        if valor_excepcion:
            log.error(f'''Ha ocurrido un error:
                      {tipo_excepcion}
                      {valor_excepcion}
                      {detalle_excepcion}''')
            self._conn.rollback()
        else:
            log.debug('Commit de la transacción')
            self._conn.commit()
        self._cursor.close()
        Conexion.liberarConexion(self._conn)

if __name__ == "__main__":
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque WITH')
        cursor.execute('SELECT * FROM persona ORDER BY id_persona')
        log.debug(cursor.fetchall())
