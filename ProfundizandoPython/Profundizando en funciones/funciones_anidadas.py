# Definir una función dentro de otra


def calculadora(a, b, operacion = 'Sumar'):
    # Primero la definimos
    def sumar(a, b):
        return a + b

    def restar(a , b):
        return a - b
    # Después la llamamos
    print(sumar(a, b))
    print(restar(a , b))

    if operacion == 'Sumar':
        print(sumar(a, b))
    else:
        print(restar(a, b))


calculadora(2, 3, 'Sumar')
calculadora(2, 3, 'Restar')