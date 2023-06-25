

class Persona:

    def __init__(self, id_persona = None, nombre = None, apellido = None, email = None) -> None:
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    def __str__(self) -> str:
        return f'''
        Id_persona -> {self._id_persona}
        Nombre -> {self._nombre}
        Apellido -> {self._apellido}
        Email -> {self._email}
        '''

    @property
    def id_persona(self):
        return self._id_persona
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @property
    def email(self):
        return self._email
    
    @id_persona.setter
    def id_persona(self, nuevo_valor):
        self._id_persona = nuevo_valor

    @nombre.setter
    def nombre(self, nuevo_valor):
        self._nombre = nuevo_valor

    @apellido.setter
    def apellido(self, nuevo_valor):
        self._apellido = nuevo_valor
    
    @email.setter
    def email(self, nuevo_valor):
        self._email = nuevo_valor


if __name__ == "__main__":
    persona1 = Persona(1, 'German', 'Martinez', 'gmartinez@email.com')
    print(persona1)