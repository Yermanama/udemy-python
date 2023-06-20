class Persona:
    def __init__(self, nombre, edad) -> None:
        self._nombre = nombre
        self._edad = edad
    
    def __add__(self, other):
        return self._nombre + other._nombre
    
    def __sub__(self, other):
        return self._edad - other._edad

"""
Cuando hacemos esta operación:

objeto1 + objeto2

De la manera en que funciona por dentro pythone es la siguiente:

objeto1.__add__(objeto2)

"""

persona1 = Persona('Juan', 10)
persona2 = Persona('Carlos', 5)

print(persona1 + persona2)
print(persona1 - persona2)

