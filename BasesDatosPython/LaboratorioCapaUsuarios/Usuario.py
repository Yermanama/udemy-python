class Usuario:

    def __init__(self, id_usuario: int, username: str, password: str) -> None:
        self._id_usuario = id_usuario
        self._username = username
        self._password = password

    @property
    def id_usuario(self):
        return self._id_usuario
    
    @property
    def username(self):
        return self._username
    
    @property
    def password(self):
        return self._password
    
    @id_usuario.setter
    def id_usuario(self, nuevo_valor: int):
        self._id_usuario = nuevo_valor
    
    @username.setter
    def username(self, nuevo_valor: str):
        self._username = nuevo_valor

    @password.setter
    def password(self, nuevo_valor: str):
        self._password = nuevo_valor

    def __str__(self) -> str:
        return f'''
        Id_usuario -> {self._id_usuario}
        Username -> {self._username}
        Password -> {self._password}
        '''
    

if __name__ == "__main__":
    usuario1 = Usuario(1, 'usuario', 'contraseña')
    print(usuario1)