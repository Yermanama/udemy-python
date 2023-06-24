from logger_base import root_logger

class Persona:
    def __init__(self, id_persona=None, nombre=None, apellido=None, mail=None) -> None:
        self._nombre = nombre
        self._apellido = apellido
        self._mail = mail
        self._id_persona = id_persona

    def __str__(self) -> str:
        return f'''
        Id persona: {self._id_persona} | Nombre: {self._nombre}
        Apellido: {self._apellido} | Mail: {self._mail}
        '''
    
    @property
    def id_persona(self):
        return self._id_persona
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def mail(self):
        return self._mail
    
    @property
    def apellido(self):
        return self._apellido
    
    @id_persona.setter
    def id_persona(self, nuevo_valor):
        self._id_persona = nuevo_valor
    
    @nombre.setter
    def nombre(self, nuevo_valor):
        self._nombre = nuevo_valor

    @mail.setter
    def mail(self, nuevo_valor):
        self._mail = nuevo_valor

    @apellido.setter
    def apellido(self, nuevo_valor):
        self._apellido = nuevo_valor


if __name__ == "__main__":
    persona1 = Persona('Javier', 'Gonzalez', 'jgonzalez@mail.com', 14)
    root_logger.debug(persona1)