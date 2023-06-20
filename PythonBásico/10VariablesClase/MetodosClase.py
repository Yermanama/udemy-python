class Clase:
    
    variable_clase = "Esto es una variable de clase"

    def __init__(self, variable_instancia) -> None:
        self.variable = variable_instancia

    # Para crear un metodo estático debemos de usar un decorador
    @staticmethod
    def metodo_estatico(): # Un método estático, no puede acceder a las variables de instancia, por ello no accede tampoco a self
        # Pero si que podemos acceder a las variables de clase, pero de manera indirecta
        print(Clase.variable_clase)
    
    # Para crear un metodo de clase debemos de usar un decorador también
    @classmethod
    def metodo_clase(cls): # Cls hace referencia a nuestra clase, por lo que podemos acceder a las variables de nuestra clase
        print(cls.variable_clase)

    # Desde un metodo de instancia, si que podemos acceder al resto de metodos de la clase
    # También podemos acceder a los valores de clase, y por supuesto a los valores de instancia
    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.varible_instancia)

# Para acceder al método estático lo tenemos que hacer a través de la clase
Clase.metodo_estatico()