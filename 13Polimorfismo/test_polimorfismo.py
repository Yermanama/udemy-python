from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalles(objeto):
    """El polimorfismo se aplica aquí debido a que 
    cuando mandemos imprimir se comportará de manera distinta según el método str de cada uno"""
    print(objeto)
    print(type(objeto))
    if isinstance(objeto, Gerente):
        print(objeto._departamento)

empleado = Empleado('Juan', 20000)
imprimir_detalles(empleado)

gerente = Gerente('Antonio', 50000, 'tecnología')
imprimir_detalles(gerente)