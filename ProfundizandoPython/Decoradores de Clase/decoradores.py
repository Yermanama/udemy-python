# Decoradores de clase
# Permiten transformar de manera programática nuestra clase
# Similar a los decoradores de funciones (Metaprogramación)

import inspect


def decorador_repr(cls):
    print('Se ejecuta decorador')
    print(f'Recibimos el objeto de la clase: {cls.__name__}')

    # Revisamos los atributos de la clase con el método vars
    atributos = vars(cls)
    # Iteramos cada atributo (vienen en diccionario)
    for name, valor in atributos.items():
        print(name, valor)

    # Revisamos si se ha sobreescrito el método __init__
        if '__init__' not in atributos:
            raise TypeError(f'{cls.__name__} no ha sobreescrito el método __init__')
        
    firma_init = inspect.signature(cls.__init__)
    print(f'Firma del método __init__: {firma_init}')
    # Recuperamos los parámetros excepto el primero que es self
    parametros_init = list(firma_init.parameters)[1:]
    print(f'Parametros init: {parametros_init}')

    # Revisamos si cada parámetro tiene un metodo property asocidado
    for parametro in parametros_init:
        # property es unvalor de tipo built-in para preguntar si se está utilizando al decorar property
        es_metodo_property = isinstance(atributos.get(parametro), property)
        if not es_metodo_property:
            raise TypeError(f'No existe un método property para el parámetro {parametro}')
        
    
    # Crear el método repr dinámicamente
    def metodo_repr(self):
        # Obtenemos el nombre de la clase dinámicamente
        nombre_clase = self.__class__.__name__
        print(f'Nombre clase: {nombre_clase}')

        # Obtenemos los nombres y contenidos de las propiedades dinámicamente
        # Expresion generadora, para crear nombre_art = valor_atr
        generador_arg = (f'{nombre}={getattr(self, nombre)!r}' for nombre in parametros_init)
        # Lista del generador
        lista_arg = list(generador_arg)
        print(f'Lista del generador: {lista_arg}')

        # Creamos la cadena a partir de la lista de argumentos
        argumentos = ', '.join(lista_arg)
        print(f'Argumentos del método repr {argumentos}')
        # Creamos la forma del método __repr__, sin su nombre
        resultado_metodo_repr = f'{nombre_clase}({argumentos})'
        print(f'Resultado metodo repr {resultado_metodo_repr}')
        return resultado_metodo_repr

 
    # Para agregar dinámica el método repr a nuestra clase
    setattr(cls, '__repr__', metodo_repr)

    # Hacemos esto porque necesitamos terminar de crear nuestro objeto, si no, no funcionará 
    return cls


@decorador_repr
class Persona:

    def __init__(self, nombre, apellido):
        print('Se ejecuta el inicializador')
        self._nombre = nombre
        self._apellido = apellido
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def apellido(self):
        return self._apellido



persona = Persona('Juan', 'Perez')
print(persona)

# Comprobamos si tiene los métodos nombre, apellido, repr
print(dir(Persona))

# Tiene el método repr sobreescrito
codigo_repr = inspect.getsource(persona.__repr__)
print(codigo_repr)