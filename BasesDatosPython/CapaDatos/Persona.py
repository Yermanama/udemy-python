from logger_base import log

class Persona:
    def __init__(self, id_persona = None, nombre=None, apellido=None, email=None) -> None:
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    @property
    def id_persona(self):
        return self._id_persona
    
    @id_persona.setter
    def id_persona(self, nuevo_id):
        self._id_persona = nuevo_id

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, nuevo_apellido):
        self._apellido = nuevo_apellido

    @property
    def email(self):
        return self._nombre
    
    @email.setter
    def email(self, nuevo_email):
        self._email = nuevo_email

    def __str__(self) -> str:
        return f'''
        Id_persona -> {self._id_persona} | Nombre -> {self._nombre}
        Apellido -> {self._apellido} | Email -> {self._apellido}
        '''
    

if __name__ == "__main__":
    persona1 = Persona(1, 'Juan', 'Perez', 'jperez@mail.com')
    log.debug(persona1)
    # Simular un insert
    persona1 = Persona(nombre='Juan', apellido='Perez', email='jperez@mail.com')
    log.debug(persona1)
    # Simular un delete
    persona1 = Persona(id_persona=1)
    log.debug(persona1)