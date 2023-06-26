from UsuarioDAO import UsuarioDAO
from Usuario import Usuario
from logger_base import root_logger as log

    
def listar_usuarios():
    lista_usuarios = UsuarioDAO.seleccionar()
    for usuario in lista_usuarios:
        log.info(usuario)

def agregar_usuario():
    input_username_usuario = input('Introduce el nombre del usuario. ')
    input_password_usuario = input('Inserta la constraseña del usuario. ')
    if input_username_usuario and input_password_usuario:
        usuario1 = Usuario(username=input_username_usuario, password=input_password_usuario)
        usuario_insertado = UsuarioDAO.insertar(usuario1)
        log.info(f'Usuario insertado -> {usuario_insertado}')
    else:
        log.error('El nombre del usuario y/o la contraseña no pueden estar vacías.')

def actualizar_usuario():
    try:
        input_id_usuario = int(input('Introduce el id_usuario que quieres que se actualice. '))
        input_username_usuario = input('Introduce el username a actualizar. ')
        input_password_usuario = input('Introduce la contraseña a actualizar. ')
        usuario1 = Usuario(id_usuario=input_id_usuario, username=input_username_usuario, password=input_password_usuario)
        usuario_actualizado = UsuarioDAO.actualizar(usuario1)
        log.info(f'Usuario actualizado -> {usuario_actualizado}')
    except ValueError:
        log.error('El id_usuario debe de ser un entero.')

def eliminar_usuario():
    try:
        input_id_usuario = int(input('Introduce el id_usuario del usuario que quieres eliminar. '))
        usuario1 = Usuario(id_usuario= input_id_usuario)
        usuario_eliminado = UsuarioDAO.eliminar(usuario1)
        log.info(f'Usuario eliminado -> {usuario_eliminado}')
    except ValueError:
        log.error('El valor de id debe de ser un entero.')

def main():
    valor = 0
    while valor != 5:
        print('¿Qué deseas hacer ahora? Elige un número del 1 al 5:')
        print('1. Listar usuarios')
        print('2. Agregar usuario')
        print('3. Actualizar usuario')
        print('4. Eliminar usuario')
        print('5. Salir')
        valor = int(input())
        if valor == 1:
            listar_usuarios()
        elif valor == 2:
            agregar_usuario()
        elif valor == 3:
            actualizar_usuario()
        elif valor == 4:
            eliminar_usuario()
        elif valor == 5: 
            log.info('Saliendo del programa...')
        else:
            log.error('Por favor, introduce un valor entre el 1 y el 5.')


if __name__ == "__main__":
    main()