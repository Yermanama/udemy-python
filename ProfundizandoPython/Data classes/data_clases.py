import dataclasses
import typing


@dataclasses.dataclass(eq=True, frozen=True)
class Domicilio:
    calle: str
    numero: int = 0


@dataclasses.dataclass(eq=True, frozen=True)
class Persona:
    nombre: str
    apellido: str
    domicilio: Domicilio
    contador_persona : typing.ClassVar[int] = 0 

    def __post_init__(self):
        if not self.nombre:
            raise ValueError(f'Valor nombre vacío: {self.nombre}')


domicilio1 = Domicilio('Saturno', 15)

persona1 = Persona('Juan', 'Perez', domicilio1)
print(persona1)
# Variable de clase
print(f'Variable de clase : {Persona.contador_persona}')

# Variables de instancia
print(f'Variables de instancia: {persona1.__dict__}')

# Variable con valores vacíos
'''persona_vacia = Persona('', '')
print(persona_vacia)'''

# revisar igualdad entre objetos -> __eq__
persona2 = Persona('Juan', 'Perez', Domicilio('Jupiter', 30))
print(f'Personas iguales?: {persona1 == persona2}')

# Agregar esta clase a una coleccion
coleccion = {persona1, persona2} # Esto nos da error porque estos objetos no son de clase inmutable

# Después de añadir el parámetro de frozen = true, ya no son mutables
print(coleccion)
# coleccion[0].nombre = 'Juan Carlos' -> Por lo que esto ahora nos da error porque están frozen (inmutables)