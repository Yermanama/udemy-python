"""
Ejercicio: Convertidor de Temperatura
Realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa.

formula celsius a f = ( °C × 9 / 5) + 32 =  °F
formula f a c = ( °F − 32) × 5 / 9 =  °C
"""


def celsius_a_fahrenheit(temperatura):
    return (temperatura*(9/5)) + 32


def fahrenheit_a_celsius(temperatura):
    return (temperatura - 32) * (5/9)


def convertidor_temperatura(temperatura: int, unidad: str):
    if unidad == "C":
        temp_convertida = celsius_a_fahrenheit(temperatura)
        print(f"La conversión es que estás a {temp_convertida} grados Fahrenheit")
    elif unidad == "F":
        temp_convertida = fahrenheit_a_celsius(temperatura)
        print(f"La conversión es que estás a {temp_convertida} grados Celsius")
    else:
        print("Por favor, introduce una unidad correcta.")

if __name__ == "__main__":
    temperatura = int(input("Por favor, introduce la temperatura a la que estáis: "))
    unidad = input("Por favor, introduce la métrica que estas usando: ['C' o 'F']")
    convertidor_temperatura(temperatura, unidad)