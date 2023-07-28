# Orden de inicialización de los objetos

class Padre:
    def __init__(self) -> None:
        print('Inicializador Padre')

    def metodo(self):
        print('Metodo padre')



class Hijo(Padre):
    # Se manda llamar el método init de la clase padre
    # siempre y cuando la clase hija no defina su propio metodo init

    # definimos el metodo init de la clase hija (se sobreescribe el de la clase padre)
    def __init__(self) -> None:
        # De manera opcional podemos llamar al metodo init de la clase padre (super)
        print('Inicializador de la clase hija')
        super().__init__()
    
    # Sobreescribimos el metodo heredado de la clase padre
    def metodo(self):
        print('Metodo sobreescrito hijo')
        # De manera opcional podemos llamar al metodo del padre
        super().metodo()

# padre1 = Padre()
# padre1.metodo()

hijo1 = Hijo()
hijo1.metodo()