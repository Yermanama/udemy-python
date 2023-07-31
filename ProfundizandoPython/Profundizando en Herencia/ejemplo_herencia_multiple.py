class Clase1:
    def __init__(self) -> None:
        print('Clase 1 Init')

    def metodo(self):
        print('Metodo de la clase 1')


class Clase2(Clase1):

    def __init__(self) -> None:
        print('Clase 2 Init')
        super().__init__()

    def metodo(self):
        print('Metodo de clase 2')
        super().metodo()

class Clase3(Clase1):

    def __init__(self) -> None:
        print('Clase 3 Init')
        super().__init__()

    def metodo(self):
        print('Metodo Clase 3')
        super().metodo()

class Clase4(Clase2, Clase3):
    def __init__(self) -> None:
        print('Clase 4 Init')
        super().__init__()

    def metodo(self):
        print('Metodo clase 4')
        super().metodo()


class Clase5(Clase4, Clase2):
    def __init__(self) -> None:
        print('Clase 5 Init')
        super().__init__()

    def metodo(self):
        print('Metodo clase 5')
        super().metodo()


clase1 = Clase1()
clase1.metodo()

clase2 = Clase2()
clase2.metodo()

clase3 = Clase3()
clase3.metodo()

clase4 = Clase4()
clase4.metodo()
print(Clase4.__bases__)
print(Clase4.mro())

clase_5 = Clase5()
clase_5.metodo()
print(Clase5.__bases__)
print(Clase5.mro())