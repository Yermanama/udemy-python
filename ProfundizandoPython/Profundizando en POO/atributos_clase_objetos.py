class Persona:
    contador_persona = 0

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


# Mostrar los atributos de un OBJETO, no vamos a ver los atributos de instancia o de clase
persona1 = Persona("Juan", "Perez")
print(persona1.__dict__)

# Crear un atributo al vuelo
print(persona1.contador_persona)  # Aquí accedemos al atributo de clase
# Pero no es posible modificarlo con el objeto, sino con la clase
# Lo que si modificamos es el valor del objeto
persona1.contador_persona = 10  # Aquí podríamos pensar que estamos accediendo al valor de clase, pero no es así, solo lo podríamos leer, pero no editar

print(persona1.__dict__)

# El atributo anterior oculta el atributo de clase
# SI queremos acceder al atributo de clase, debemos de hacerlo a través de la clase misma
print(Persona.contador_persona) # Aquí accedemos al atributo de la clase
print(persona1.contador_persona) # Aquí accedemos al atributo del objeto

# Si creamos un segundo objeto, no vamos a tener el valor creado en el primero objeto, si no los creados en la clase
persona2 = Persona('Karla', 'Lopez')
print(persona2.__dict__)
print(persona2.contador_persona)

# Asociar un atributo de clase al vuelo
# print(Persona.contador2) -> Esto da error porque no está creado todavía
Persona.contador2 = 20
print(Persona.contador2)