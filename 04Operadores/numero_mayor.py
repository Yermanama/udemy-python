"""
Instrucciones de tareas:
Solicitar al usuario dos valores, y determinar cuál número es el mayor
Solicitar al usuario dos valores:
numero1 (int)
numero2 (int)
Se debe imprimir el mayor de los dos números (la salida debe ser idéntica a la que sigue):
Proporciona el numero1:
Proporciona el numero2:
El número mayor es:<numeroMayor>
"""

numero1: int = int(input('Introduce el primer número, por favor: \n'))
numero2: int = int(input('Introduce el segundo número, por favor: \n'))

if numero1 == numero2:
    print('Los dos números son el mismo.')
elif numero1 > numero2:
    print(f'El número {numero1} es el mayor.')
else:
    print(f'El número {numero2} es el mayor.')
