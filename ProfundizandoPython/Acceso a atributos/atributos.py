# ejemplo atributos publicos, protegidos, privados

class MiClase:
    def __init__(self, publico, protegido, privado) -> None:
        self.publico = publico
        # Si solo queremos usarlo dentro de esta clase o dentro de una subclase
        self._protegido = protegido
        # Si solo queremos acceder a este dentro de esta clase, ni de una subclase si quiera
        self.__privado = privado

    
objeto = MiClase('Valor público', 'Valor protegido', 'Valor privado')
# Acceso al atributo público
print(objeto.publico)
objeto.publico = 'Nuevo valor público'
print(objeto.publico)
# Acceso al valor protegido
# Solo dentro de esta misma clase, o clases hijas (lo que estamos haciendo no es una buena práctica)
print(objeto._protegido)
objeto._protegido = 'Nuevo valor protegido'
print(objeto._protegido)
# Acceso al valor privado
# print(objeto.__privado)
# Pero, python convierte el valor privado a: _NOMBRECLASE__NOMBREATRIBUTO
print(objeto._MiClase__privado)
# Modificar valor privado
objeto._MiClase__privado = 'Nuevo valor privado'
print(objeto._MiClase__privado)