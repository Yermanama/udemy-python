"""
Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas.
Puede ser cualquier valor positivo, ejemplo, si pasamos el valor de 5, debe imprimir:
5
4
3
2
1

En caso de pasar el valor de 3, debe imprimir:
3
2
1

Si se pasan valores negativos no imprime nada
"""

def imprimir_numeros_recursivamente(numero : int):
    if numero > 0:
        print(numero)
        imprimir_numeros_recursivamente(numero - 1)

if __name__ == "__main__":
    imprimir_numeros_recursivamente(5)
    imprimir_numeros_recursivamente(3)
    imprimir_numeros_recursivamente(-1)
