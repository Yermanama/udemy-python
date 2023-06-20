"""
Ejercicio: Calculadora de Impuestos
Crear una función para calcular el total de un pago incluyendo un impuesto aplicado.
# Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
"""

def pago_impuesto(bruto: int, porcentaje: int) -> float:
    return bruto + (bruto * (porcentaje/100))

if __name__ == "__main__":
    bruto = int(input("Por favor, indica en números enteros el pago en bruto: "))
    porcentaje = int(input("Ahora indica el porcentaje que se debe aplicar: "))
    print(pago_impuesto(bruto, porcentaje))