from logger_base import root_logger as log
from CursorDelPool import CursorDelPool
from Usuario import Usuario

class UsuarioDAO:
    '''
    DAO -> Data Access Object
    CRUD -> Create-Read-Update-Delete
    '''

    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username, password) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario = %s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'


    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios
        
    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Usuario insertado correctamente -> {usuario}')
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Usuario actualizado -> {usuario}')
            return cursor.rowcount
        
    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            id_usuario = (usuario.id_usuario, )
            cursor.execute(cls._ELIMINAR, id_usuario)
            log.debug(f'Usuario eliminado -> {usuario}')
            return cursor.rowcount
        

if __name__ == "__main__":
    usuario1 = Usuario(1, 'yermanama', 'contraseña')
    # Insertar
    UsuarioDAO.insertar(usuario1)
    # Seleccionar
    UsuarioDAO.seleccionar()
    # Actualizar
    usuario1 = Usuario(1, 'yerman', 'password')
    UsuarioDAO.actualizar(usuario1)
    # Eliminar
    UsuarioDAO.eliminar(usuario1)