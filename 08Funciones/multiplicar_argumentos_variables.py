def multiplicar_variables(*numeros: int) -> int:
    multiplicacion : int = 1
    for numero in numeros:
        multiplicacion *= numero
    return multiplicacion

if __name__ == "__main__":
    print(multiplicar_variables(2,3,4))