# Simulación de sobrecarga de constructores (No existe en python)

class Persona:

    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido

    @classmethod
    def crear_persona_vacia(cls):
        return cls(None, None)
    
    @classmethod
    # Esto es como llamar y crearlo con el método init
    def crear_persona_valores(cls, nombre, apellido):
        return cls(nombre, apellido)
    
    def __str__(self) -> str:
        return f'Nombre {self.nombre}, Apellido {self.apellido}'


# Primera forma de crear objetos
persona1 = Persona('Juan', 'Perez')
print(persona1)

# Creamos persona vacia con el método de clase
persona_vacio = Persona.crear_persona_vacia()
print(persona_vacio)

# Creamos otra persona
persona_valores = Persona.crear_persona_valores('Karla', 'Lopez')
print(persona_valores)