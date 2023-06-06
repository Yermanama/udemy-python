"""
Instrucciones de la tarea:
El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:
El usuario proporcionará un valor entre 0 y 10.
Si está entre 9 y 10: imprimir una A
Si está entre 8 y menor a 9: imprimir una B
Si está entre 7 y menor a 8: imprimir una C
Si está entre 6 y menor a 7: imprimir una D
Si está entre 0 y menor a 6: imprimir una F
cualquier otro valor debe imprimir: Valor incorrecto
Por ejemplo:
Proporciona un valor entre 0 y 10:
A
"""

nota_usuario: int = int(input('Proporciona un valor entre 0 y 10: '))

if 10 >= nota_usuario >= 9:
    print('A')
elif 9 > nota_usuario >= 8:
    print('B')
elif 8 > nota_usuario >= 7:
    print('C')
elif 7 > nota_usuario >= 6:
    print('D')
elif 6 > nota_usuario >= 0:
    print('F')
else:
    print('Valor incorrecto.')
